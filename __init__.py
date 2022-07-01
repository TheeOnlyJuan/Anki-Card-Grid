from anki import hooks

from aqt.qt import (Qt, QAction, QStandardPaths,
                    QImage, QPainter, QSize, QEvent, QSizePolicy,
                    QFileDialog, QDialog, QHBoxLayout, QVBoxLayout, QGroupBox,
                    QLineEdit, QLabel, QCheckBox, QSpinBox, QComboBox, QPushButton)
from anki.utils import ids2str
from aqt.webview import AnkiWebView
import unicodedata
import re
import urllib.parse
from functools import reduce
import enum

from . import groups
from .multiCheckBoxList import CheckableComboBox

deck_fields = dict()
colors = ['Red','Orange','Yellow','Green','Cyan','Blue','Pink','Peach','Purple']
class NoteInfo:
    def __init__(self, value):
        self.idx = 0
        self.value = value
        self.avg_interval = 0.0
        self.count = 0
        self.mod = 0
        self.decks = set()

    def addDataFromCard(self, card):
        if card.type > 0:
            newTotal = (self.avg_interval * self.count) + card.ivl

            self.count += 1
            self.avg_interval = newTotal / self.count
            self.decks.add(card.did)
class SortOrder(enum.Enum):
    NONE = 0
    UNICODE = 1
    SCORE = 2
    FREQUENCY = 3

    def pretty_value(self):
        return (
            "order found",
            "unicode order",
            "score",
            "frequency",
        )[self.value]
def hsvrgbstr(h, s=0.8, v=0.9):
    _256 = lambda x: round(x*256)
    i = int(h*6.0)
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i % 6
    if i == 0: return "#%0.2X%0.2X%0.2X" % (_256(v), _256(t), _256(p))
    if i == 1: return "#%0.2X%0.2X%0.2X" % (_256(q), _256(v), _256(p))
    if i == 2: return "#%0.2X%0.2X%0.2X" % (_256(p), _256(v), _256(t))
    if i == 3: return "#%0.2X%0.2X%0.2X" % (_256(p), _256(q), _256(v))
    if i == 4: return "#%0.2X%0.2X%0.2X" % (_256(t), _256(p), _256(v))
    if i == 5: return "#%0.2X%0.2X%0.2X" % (_256(v), _256(p), _256(q))

def scoreAdjust(score):
    score += 1
    return 1 - 1 / (score * score)

def initialize_addon():
    #TODO add initialization of settings, if any
    print('Alive')
    from aqt import mw

    #if import fails bail :(
    if not mw:
        return

    #initialize Menu UI
    menu_action = QAction("Character Grid", mw)
    menu_action.triggered.connect(lambda _: launch_options_dialog(mw))
    mw.form.menuTools.addSeparator()
    mw.form.menuTools.addAction(menu_action)

#2nd stage Menu
def launch_options_dialog(mw):
    def generate_html(notes):
        def kanjitile(char, index, count=0, avg_interval=0, missing=False):
            def scoreAdjust(score):
                score += 1
                return 1 - 1 / (score * score)
            tile = ""
            score = "NaN"

            if avg_interval:
                score = round(scoreAdjust(avg_interval / strength.value()), 2)

            # if missing:
            #     colour = "#888"
            # else:
            #     colour = "#000"
            colour = "#000"
            if count != 0:
                bgcolour = hsvrgbstr(scoreAdjust(avg_interval / strength.value()) / 2)
            elif missing:
                bgcolour = "#EEE"
            else:
                bgcolour = "#FFF"

            tooltip = "Character: %s" % char
            if count:
                tooltip += " | Count: %s | " % count
                tooltip += "Avg Interval: %s | Score: %s | " % (round(avg_interval, 2), score)
                tooltip += "Index: %s" % index
            tile += "\t<div style=\"border: black; border-width: 1px; border-style: solid; background:%s;\" title=\"%s\">" % (bgcolour, tooltip)
            # else:
            #     tile += "\t<div style=\"background:%s;\">" % (bgcolour)
            tile += "<a href=\"http://jisho.org/search/%s%%20%%23kanji\" style=\"color:%s;margin: 2px;\">%s</a></div>\n" % (
            char, colour, char)

            return tile
        html = "<!doctype html><html><head><meta charset=\"UTF-8\" /><title>Anki Character Grid</title>"
        html += "<style type=\"text/css\">body{background-color:#FFF;}.maintable{width:85%%;}.maintable,.missingtable{margin-left:auto;margin-right:auto;display:grid;grid-template-columns:repeat(%s, 1fr);text-align:left;}.maintable > *,.missingtable > *{text-align:center;vertical-align:top;margin:1px;line-height:1.5em;}.key{display:inline-block;width:3em}a,a:visited{color:#000;text-decoration:none;}</style>" % column_size.value()
        if False:#config.autothinwide:
            html += "<style type=\"text/css\">.maintable,.missingtable{display:block;font-size:0px}.maintable > *,.missingtable > *{display:inline-block;font-size:initial;width:1.5em;}</style>"
        html += "</head>\n<body>\n"

        html += "<span style=\"font-size: 2em;color: #888;\">Kanji Grid - %s</span><br>\n" % " ,".join(deck_checkbox.currentText().split('" '))
        html += '''<div style=\"margin-bottom: 24pt;padding: 20pt;\"><p style=\"float: left\">Key:</p>
                    <p style=\"float: right\">Weak&nbsp;'''
        for c in [n / 6.0 for n in range(6 + 1)]:
            html += "<span class=\"key\" style=\"background-color: %s;\">&nbsp;</span>" % hsvrgbstr(c / 2)
        html += '''&nbsp;Strong</p></div>\n
        <div style=\"clear: both;\"><br><hr style=\"border-style: dashed;border-color: #666;width: 60%;\"><br></div>\n
        <div style=\"text-align: center;\">\n'''
        if group_by.currentIndex() < len(SortOrder):
            table = "<div class=\"maintable\">\n"
            unitsList = {
                SortOrder.NONE: sorted(notes.values(), key=lambda unit: (unit.idx, unit.count)),
                SortOrder.UNICODE: sorted(notes.values(), key=lambda unit: (unicodedata.name(unit.value[0] if len(unit.value) else ''), unit.count)),
                SortOrder.SCORE: sorted(notes.values(),
                                        key=lambda unit: (scoreAdjust(unit.avg_interval / strength.value()), unit.count),
                                        reverse=True),
                SortOrder.FREQUENCY: sorted(notes.values(), key=lambda unit: (
                unit.count, scoreAdjust(unit.avg_interval / strength.value())), reverse=True),
            }[SortOrder(group_by.currentIndex())]
            count = -1
            for unit in unitsList:
                if unit.count != 0 or show_unseen.isChecked():
                    count += 1
                    table += kanjitile(unit.value, count, unit.count, unit.avg_interval)
            table += "</div>\n"
            html += "<h4 style=\"color:#888;\">%d total unique %s</h4>\n" % (count + 1, 'words' if use_entire_word.isChecked() else 'kanji')
            html += table
        else:
            g = groups.groups[group_by.currentIndex() - len(SortOrder)]
            gc = 0
            values_list = [u.value for u in notes.values()]
            print('gc')
            print(len(g.data))
            for i in range(1, len(g.data)):
                html += "<h2 style=\"color:#888;\">%s Kanji</h2>\n" % g.data[i][0]
                table = "<div class=\"maintable\">\n"
                count = -1
                for unit in [notes[c] for c in g.data[i][1] if c in values_list]:
                    if unit.count != 0 or show_unseen.isChecked():
                        count += 1
                        table += kanjitile(unit.value, count, unit.count, unit.avg_interval)
                table += "</div>\n"
                n = count + 1
                t = len(g.data[i][1])
                gc += n
                if show_unseen.isChecked():
                    table += "<details><summary>Missing kanji</summary><div class=\"missingtable\" style=\"max-width:75%;\">\n"
                    count = -1
                    for char in [c for c in g.data[i][1] if c not in values_list]:
                        count += 1
                        table += kanjitile(char, count, missing=True)
                    if count == -1:
                        table += "<b style=\"color:#CCC\">None</b>"
                    table += "</div></details>\n"
                html += "<h4 style=\"color:#888;\">%d of %d - %0.2f%%</h4>\n" % (n, t, n * 100.0 / t)
                html += table
            chars = reduce(lambda x, y: x+y, dict(g.data).values())
            html += "<h2 style=\"color:#888;\">%s Kanji</h2>" % g.data[0][0]
            table = "<div class=\"maintable\">\n"
            count = -1
            for unit in [u for u in notes.values() if u.value not in chars]:
                if unit.count != 0 or show_unseen.isChecked():
                    count += 1
                    table += kanjitile(unit.value, count, unit.count, unit.avg_interval)
            table += "</div>\n"
            n = count+1
            html += "<h4 style=\"color:#888;\">%d of %d - %0.2f%%</h4>\n" % (n, gc, 0 if gc == 0 else n*100.0/gc)
            html += table
            html += "<style type=\"text/css\">.datasource{font-style:italic;font-size:0.75em;margin-top:1em;overflow-wrap:break-word;}.datasource a{color:#1034A6;}</style><span class=\"datasource\">Data source: " + ' '.join("<a href=\"{}\">{}</a>".format(w, urllib.parse.unquote(w)) if re.match("https?://", w) else w for w in g.source.split(' ')) + "</span>"
        # print(html)
        return html
    ui = QDialog(mw)
    layout = QVBoxLayout()

    #deck selection
    deck_checkbox = CheckableComboBox()
    deck_names = mw.col.decks.allNames()
    print(deck_names)
    deck_checkbox.addItems(deck_names)
    layout.addWidget(QLabel("Decks to search:"))
    layout.addWidget(deck_checkbox)

    #field to look at
    field_checkbox = CheckableComboBox()
    def selection_changed(decknames):
        print(decknames)
        field_checkbox.clear()
        for deck_name in decknames.split('" '):
            if len(deck_name) > 0:
                field_checkbox.addItems(deck_fields[names_to_ids[deck_name]])
        field_checkbox.selectItem(0)

    #Get deck ids and mappings
    deck_ids = mw.col.decks.decks.keys()
    names_to_ids = dict()

    for deck_id in deck_ids:
        deck = mw.col.decks.get(deck_id)
        names_to_ids[deck["name"]] = deck_id

    #Default deck
    deck_fields['1'] = []
    for deck_id in deck_ids:
        card_ids = mw.col.db.list(
            "select id from cards where did in %s or odid in %s limit 1" % (ids2str([deck_id]), ids2str([deck_id])))
        for card_id in card_ids:
            deck_fields[deck_id] = mw.col.getCard(card_id).note().keys()

    print(mw.col.decks.decks.keys())
    print(mw.col.decks.get(mw.col.conf['curDeck']))
    current_deck = mw.col.conf['curDeck']
    print(current_deck)
    print(mw.col.decks.children(current_deck))
    deck_checkbox.currentTextChanged.connect(selection_changed)
    current_deck = mw.col.conf['curDeck']
    deck_checkbox.selectItemByValue(mw.col.decks.get(current_deck)["name"])
    selection_changed(deck_checkbox.currentText())
    layout.addWidget(QLabel("Fields to search:"))
    layout.addWidget(field_checkbox)


    print(deck_fields)
    print()
    #get cards
    deck_ids = [current_deck]
    card_ids = mw.col.db.list("select id from cards where did in %s or odid in %s" % (ids2str(deck_ids), ids2str(deck_ids)))
    print(len(card_ids))
    print(card_ids[0])
    card = mw.col.getCard(card_ids[0])
    print("card here")
    print(card)
    print(card.note().keys())

    #Group By
    group_layout = QHBoxLayout()
    group_by = QComboBox()
    group_by.addItems(["None, sorted by " + x.pretty_value() for x in SortOrder])
    group_by.addItems([x.name for x in groups.groups])
    #group_by.setCurrentIndex(config.group_by)
    group_layout.addWidget(QLabel("Group by:"))
    use_entire_word = QCheckBox("Group using entire word")
    group_layout.addWidget(use_entire_word)

    layout.addLayout(group_layout)
    layout.addWidget(group_by)
    show_unseen = QCheckBox("Show characters not yet seen")
    # shnew.setChecked(config.unseen)
    layout.addWidget(show_unseen)

    #colors
    color_layout = QHBoxLayout()
    weak_color = QComboBox()
    weak_color.addItems(colors)
    strong_color = QComboBox()
    strong_color.addItems(colors)
    color_layout.addWidget(QLabel("Weak Color: "))
    color_layout.addWidget(weak_color)
    color_layout.addWidget(QLabel("Strong Color: "))
    color_layout.addWidget(strong_color)
    layout.addLayout(color_layout)

    #Other field
    strength = QSpinBox()
    strength.setRange(1, 65536)
    strength.setValue(100)
    layout.addWidget(QLabel("Card interval considered strong:"))
    layout.addWidget(strength)
    column_size = QSpinBox()
    column_size.setRange(1, 65536)
    column_size.setValue(20)
    layout.addWidget(QLabel("Number of columns:"))
    layout.addWidget(column_size)

    #action buttons
    action_buttons = QHBoxLayout()
    generate = QPushButton("Generate", clicked=ui.accept)
    action_buttons.addWidget(generate)
    cls = QPushButton("Close", clicked=ui.reject)
    action_buttons.addWidget(cls)
    layout.addLayout(action_buttons)

    ui.setLayout(layout)
    ui.resize(500, 400)
    if ui.exec_():
        mw.progress.start(immediate=True)
        fields_to_check = [ x for x in field_checkbox.currentText().split('" ')]
        deck_ids = [ names_to_ids[x] for x in deck_checkbox.currentText().split('" ')]
        for deck in deck_ids:
            for _, child_id in mw.col.decks.children(deck):
                deck_ids.append(child_id)
        print("deck ids")
        print(deck_ids)
        card_ids = mw.col.db.list(
            "select id from cards where did in %s or odid in %s" % (ids2str(deck_ids), ids2str(deck_ids)))

        notes = dict()
        def update_info(data, card, notes, individual = True):
            if individual:
                for char in data:
                    if groups.ignore.find(char) == -1:
                        if char not in notes:
                            notes[char] = NoteInfo(char)
                        notes[char].addDataFromCard(card)
            else:
                if data not in notes:
                    notes[data] = NoteInfo(data)
                notes[data].addDataFromCard(card)

        for card_id in card_ids:
            card = mw.col.getCard(card_id)
            #assume no dupe nids for now
            for key in fields_to_check:
                if key in card.note().keys():
                    update_info(card.note()[key],card, notes, (not use_entire_word.isChecked())) #TODO specify mode

        def generate_grid(notes):
            print(notes)
            html = generate_html(notes)
            ui = QDialog(mw)
            window_view = HtmlWindow()
            vl = QVBoxLayout()
            vl.setContentsMargins(0, 0, 0, 0)
            vl.addWidget(window_view)
            window_view.stdHtml(html)
            hl = QHBoxLayout()
            vl.addLayout(hl)
            # sh = QPushButton("Save HTML", clicked=lambda: self.savehtml(config))
            # hl.addWidget(sh)
            # sp = QPushButton("Save Image", clicked=self.savepng)
            # hl.addWidget(sp)
            bb = QPushButton("Close", clicked=ui.reject)
            hl.addWidget(bb)
            ui.setLayout(vl)
            ui.resize(500, 400)
            ui.show()
            return 0

        mw.progress.finish()
        generate_grid(notes)

        print("done")


class HtmlWindow(AnkiWebView):

    def __init__(self, parent=None):
        super().__init__()
        # Saved images are empty if the background is transparent; AnkiWebView
        # sets bg color to transparent by default
        self._page.setBackgroundColor(Qt.white)
        #self.save_png = ()






initialize_addon()
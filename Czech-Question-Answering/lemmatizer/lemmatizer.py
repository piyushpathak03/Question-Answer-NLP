# This file is part of MorphoDiTa <http://github.com/ufal/morphodita/>.
#
# Copyright 2015 Institute of Formal and Applied Linguistics, Faculty of
# Mathematics and Physics, Charles University in Prague, Czech Republic.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys

from ufal.morphodita import *

tagger = Tagger.load("czech-morfflex-pdt-161115.tagger")
converter = TagsetConverter.newStripLemmaIdConverter(tagger.getMorpho())

def lemmatize(text):
    forms = Forms()
    lemmas = TaggedLemmas()
    tokens = TokenRanges()
    tokenizer = tagger.newTokenizer()
    if tokenizer is None:
        sys.stderr.write("No tokenizer is defined for the supplied model!")
        sys.exit(1)

    # Tag
    output = []
    tokenizer.setText(text)
    while tokenizer.nextSentence(forms, tokens):
        tagger.tag(forms, lemmas)

        for i in range(len(lemmas)):
            converter.convert(lemmas[i])
            output.append(lemmas[i].lemma)

    return " ".join(output)

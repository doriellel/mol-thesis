from nltk.corpus import wordnet as wn

def extend_word_list(cat,pos):

    """
    this function takes a list of anthropomorphizing words and extends it with similar words from WordNet.

    :param cat: category of sentences corresponding to the conceptual model,
    e.g. arg0_verbs are predicates whose arg0 is anthropomorphic
    :type cat: string
    :param pos: WordNet POS (v for verb, a for adjective, n for noun)
    :type pos: string
    :return: return a list of strings
    """ 
    
    stop_words = ['fuck','shit'] # silly stop word list to exclude cases like the biblical sense of 'know'

    with open(f"../gazetteers/{cat}.txt","r") as file:
        words = [word.strip() for word in file.readlines()]
        word_list = []
    
        for word in words:
        
            for syn in [syn for syn in wn.synsets(word) if syn.pos() == pos]: # get synonyms of the same POS

                if not any(stopword in syn.lemma_names() for stopword in stop_words): # exclude synonyms containing stop words as lemmas
                    processed_lemmas = list(set([lemma.replace("_", " ") for lemma in syn.lemma_names()])) # only unique lemmas

                    also_sees = [x for x in syn.also_sees() if x.pos() == pos]
                    similar_tos = [x for x in syn.similar_tos() if x.pos() == pos]
                    related_words = also_sees + similar_tos # get also semantically similar words of the same POS

                    processed_related_words = []

                    for rel in related_words:
                        processed_related_words.extend([lemma.replace("_", " ") for lemma in rel.lemma_names()])

                    all_processed = list(set(processed_lemmas+processed_related_words))
                    word_list.extend(all_processed)

        word_list.extend(words) # add original words
        extended_word_list = list(set(word_list)) # remove duplicates

    return extended_word_list




    

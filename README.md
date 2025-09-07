## MoL thesis: A Linguistically Grounded Evaluation of Anthropomorphic Language Detection in AI Research

This repository contains code for retrieving and pre-processing data used towards the compilation of AnthroSet - an evaluation set developed as part of the MoL thesis work. 
Additionally, it contains auxiliary scripts for post-processing the results of the evaluation, and measuring the results in terms of precision, recall, F1, and accuracy, and examining prediction trends.

#### /code

1. get_sentences.ipynb: code that extracts data from the arXiv and ACL anthology corpora, including specific functionalities for identifying candidates for anthropomorphic structures (manual review is necessary).
2. validate_sentences.ipynb: validate annotated sets according to specific criteria (avoid duplicate sentences, conflicting annotations, etc)
3. calculate_IAA.ipynb: calculate IAA on 20% of the data based on redundant annotations, using Cohen's kappa
4. get_masks_and_context.ipynb: code that obtains masked sentences for each masking strategy (anthroscore and minimal entity masking)
5. get_final_evaluation_sets.ipynb: creates final evaluation sets with uniform configuration
6. evaluation.ipynb: obtain precision, recall, F1, and accuracy scores as well as prediction trends for final results.

auxiliary processing notebooks:

7. anthroscore_preprocessing.ipynb
8. conversion_utils.ipynb

/code/tools/wordnet_syns.py: obtain wordnet synsets, as well as conceptually simnilar words for entries in the wordlists

#### /data

1. IAA: IAA sets
2. candidate_sentences: preprocessed, untagged pool of candidate sentences collected automatically -- requires manual review
3. dataframes: dataframe equivalents of candidate sentences, including also previous and next sentences
4. evaluation_sentences_csv: selected and annotated sentences in csv format
5. evaluation_sentences_txt: selected and annotated sentences in txt format

#### /experiment_1
input and output files for experiment 1, using both anthroscore and atypicalanimacy models

#### /experiment_2
input and output files for experiment 2, using both anthroscore and atypicalanimacy models

#### /final_sets
uniform configuration of outputs from both experiments and both models, including expectations and predictions

#### /wordlists
txt files containing anthropomorphic verbs/nouns/adjectives (1-token per line)

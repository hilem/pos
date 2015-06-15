##### 1) Multiple noun types
> Kosgi Santosh sent an email to Stanford University. He didn't get a reply.
{
  nouns: [
    "Kosgi Santosh",
    "reply",
    "Stanford University",
    "email"
  ]
}

##### 2) Split compound noun
> Just go to Community College of Philadelphia and take a quick summer class.
{
  nouns: [
    "summer class",
    "Community College of Philadelphia",
    "Philadelphia"
  ]
}

## TODO:
##### 3) Two distinct compound nouns sharing a common word, plus possessive compounds
> Community College of Philadelphia and Purdue's College of Science go head-to-head.
Currently Producing: {
  nouns: [
    "Purdue 's College of Science",
    "Science",
    "Purdue",
    "Philadelphia",
    "Community College of Philadelphia and Purdue 's College of Science",
    "to-head"
  ]
}
Log Ouput:
(Community, NOUN, compound HEAD College, l#0, r#0, iob=3)
(College, NOUN, nsubj HEAD go, l#1, r#3, iob=1)
join result |Community College of Philadelphia and Purdue 's College of Science|
(of, ADP, prep HEAD College, l#0, r#1, iob=1)
(Philadelphia, NOUN, pobj HEAD of, l#0, r#0, iob=1)
join result |Philadelphia|
(and, CONJ, cc HEAD College, l#0, r#0, iob=2)
(Purdue, NOUN, poss HEAD College, l#0, r#1, iob=3)
join result |Purdue|
('s, PRT, case HEAD Purdue, l#0, r#0, iob=1)
(College, NOUN, conj HEAD College, l#1, r#1, iob=1)
join result |Purdue 's College of Science|
(of, ADP, prep HEAD College, l#0, r#1, iob=1)
(Science, NOUN, pobj HEAD of, l#0, r#0, iob=1)
join result |Science|
(go, VERB, ROOT HEAD go, l#1, r#2, iob=2)
(head, ADV, compound HEAD to-head, l#0, r#0, iob=2)
(-, PUNCT, punct HEAD to-head, l#0, r#0, iob=2)
(to-head, NOUN, dobj HEAD go, l#2, r#0, iob=2)
join result |to-head|
(., PUNCT, punct HEAD go, l#0, r#0, iob=2)

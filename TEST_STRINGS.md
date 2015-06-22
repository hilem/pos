##### 1) Multiple noun types
> Kosgi Santosh sent an email to Stanford University. He didn't get a reply.
>> {
      nouns: [
        "Kosgi Santosh",
        "reply",
        "Stanford University",
        "email"
      ]
    }

##### 2) Split compound noun
> Just go to Community College of Philadelphia and take a quick summer class.
>> {
      nouns: [
        "summer class",
        "Community College of Philadelphia",
        "Philadelphia"
      ]
    }

##### 3) Two distinct compound nouns sharing a common word, 
####     plus possessive compounds and a compound adverb
> Community College of Philadelphia and Purdue's College of Science go head-to-head.
>> {
      nouns: [
        "Purdue",
        "Science",
        "Purdue's College of Science",
        "Philadelphia",
        "Community College of Philadelphia",
        "head-to-head"
      ]
    }

##### 4) Same as (2) but all lowercase
> just go to community college of philadelphia and take a quick summer class
>> {
      nouns: [
        "summer class",
        "community college of philadelphia",
        "philadelphia"
      ]
    }

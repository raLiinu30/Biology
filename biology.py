#Python code that determines the syndrome based on inputted chromosomal abnormalities

name = input('Hello, what is your name? ')
question = input('Hi '+name+', what are your sex chromosomes? ')

data = {
    '1': 'You have Chromosome 1q21.1 duplication syndrome. This disorder is characterized by a large head size (macrocephaly), mild to moderate developmental delay and learning difficulties, autism or autistic-like behavior, heart problems, seizures, and/or and distinctive facial features.',
    '2': 'You have Trisomy 2 mosaicism. This disorder is characterized by intrauterine growth restriction (IUGR), any of various birth defects, distinctive facial features, growth delay, developmental delays, and intellectual disabilities.',
    '3': 'You have Trisomy 3q2. This disorder is characterized by mental retardation, moderate to severe developmental delays, abnormally diminished muscle tone (hypotonia), distinctive abnormalities of the head and facial (craniofacial) area, and/or additional physical abnormalities.',
    '4': 'You have Trisomy 4p. This disorder is characterized by growth deficiency before and after birth (prenatal and postnatal growth retardation), feeding problems during early infancy, and increased muscle tone (hypertonia) in the first months of life, followed by diminished muscle tone (hypotonia).' ,
    '5': 'You have Trisomy 5p. This disorder is characterized by growth delays after birth, malformations of the head and facial (craniofacial) area, and abnormalities of the hands and feet.',
    '6': 'You have Partial Trisomy 6q. This disorder is characterized by growth delays before and after birth, severe to profound mental retardation, a delay in the acquisition of skills requiring coordination of muscular and mental activity (psychomotor retardation), distinctive malformations of the skull and facial (craniofacial) region, musculoskeletal abnormalities, and/or additional physical features.',
    '7': 'You have Partial Monosomy 7p. This disorder is characterized by growth deficiency, musculoskeletal abnormalities, genital defects, structural malformations of the heart that are present at birth (congenital heart defects), and/or other abnormalities.',
    '8': 'You have Mosaic trisomy 8. This disorder is characterized by brain malformations, highly arched or cleft palate, shortened neck with extra skin folds, long slim body with a narrow chest, shoulders, and pelvis and kidney and cardiac abnormalities.' ,
    '9':  'You have Mosaic Trisomy 9. This disorder is characterized by growth deficiency beginning before birth, failure to grow and gain weight at the expected rate (failure to thrive) during infancy, and low muscle tone (hypotonia).',
    '10': 'You have Distal Trisomy 10q. This disorder is characterized by abnormally slow growth before and after birth, malformations of the head and facial (craniofacial) area, a small nose with turned up nostrils (anteverted nares) and a broad, flat, and/or depressed nasal bridge, a small, bow-shaped mouth with a prominent upper lip,  an unusually small lower jaw, and/or, in some patients, incomplete closure of the roof of the mouth (cleft palate).',
    '11': 'You have Partial Trisomy 11q. This disorder is characterized by growth retardation before and after birth, delayed acquisition of skills requiring the coordination of mental and motor activities (psychomotor retardation), mild to moderate mental retardation, and distinctive craniofacial abnormalities.',
    '12': 'You have Trisomy 12p. This disorder is characterized by macrocephaly (unusually large head), abnormal muscle tone, characteristic facial features, developmental delay and intellectual disability.',
    '13': 'You have Patau syndrome or Trisomy 13. This disorder is characterized by severe intellectual disability and many physical abnormalities, such as congenital heart defects, brain or spinal cord abnormalities, very small or poorly developed eyes (microphthalmia), extra fingers or toes, cleft lip with or without cleft palate, and weak muscle tone (hypotonia).',
    '14': 'You have Mosaic Trisomy 14. This disorder is characterized by rowth delays before birth (intrauterine growth retardation), failure to grow and gain weight at the expected rate (failure to thrive) during infancy, delays in the acquisition of skills requiring the coordination of mental and physical abilities (psychomotor delays), and mental retardation.',
    '15': 'You have Trisomy 15q. This disorder is characterized by developmental delay, intellectual disability, hypotonia (low muscle tone), seizures; high and/or cleft palate (roof of the mouth), scoliosis; slow growth, communication difficulties, behavioral problems, and distinctive facial features.',
    '16': 'You have Trisomy 16. This disorder is characterized by cardiac malformations, hypospadias, two vessel cords, clinodactyly and pulmonary hypoplasia.',
    '17': 'You have Trisomy 17. This disorder is characterized by developmental delays, body asymmetry, slow growth, and cerebellar hypoplasia.',
    '18': "You have Edwards' syndrome or Trisomy 18. This disorder is characterized by slow growth before birth (intrauterine growth retardation), a low birth weight, heart defects and abnormalities of other organs that develop before birth, a small, abnormally shaped head, a small jaw and mouth, and clenched fists with overlapping fingers.",
    '19': 'You have Mosaic Trisomy 19. This disorder is characterized by hydrops, epicanthal fold, hypertelorism, flat nasal bridge, short nose, small mouth, low-set and malformed ears, narrow meati, short neck with excessive skin, short chest, and protuberant abdomen.' ,
    '20': 'You have Trisomy 20. This disorder is characterized by spinal abnormalities (including spinal stenosis, vertebral fusion, and kyphosis), hypotonia (decreased muscle tone), lifelong constipation, sloped shoulders, and significant learning disabilities despite normal intelligence.',
    '21': 'You have Down sydrome or Trisomy 21. This disorder is characterized by a round face, skin fold at inner corner of eye, flattened nose bridge, small, irregular teeth, short stature, heart defects, susceptibility to respiratory infections, Leukemia, Alzheimer’s disease, and a life span shorter than normal.',
    '22': 'You have Mosaic Trisomy 22. This disorder is characterized by growth and developmental delays, asymmetric body development, and congenital heart diseases.',
    '23': 'You have an extra X chromosome. However, you may notice there is not much different about you from the outside. The reason is females with an extra X chromosome cannot be distinguished from XX females except by karyotype. '
    }
if question == 'XX':
    print('You are biologically female.')
    question2 = input('Do you have an extra copy of any chromosome? ')
    if question2 == 'Yes' or question2 == 'yes':
        question3 = input('On which chromosome do you have an extra copy? ')
        print(data[question3])
        
data1 =  {
    '1': 'You have Chromosome 1q21.1 duplication syndrome. This disorder is characterized by a large head size (macrocephaly), mild to moderate developmental delay and learning difficulties, autism or autistic-like behavior, heart problems, seizures, and/or and distinctive facial features.',
    '2': 'You have Trisomy 2 mosaicism. This disorder is characterized by intrauterine growth restriction (IUGR), any of various birth defects, distinctive facial features, growth delay, developmental delays, and intellectual disabilities.',
    '3': 'You have Trisomy 3q2. This disorder is characterized by mental retardation, moderate to severe developmental delays, abnormally diminished muscle tone (hypotonia), distinctive abnormalities of the head and facial (craniofacial) area, and/or additional physical abnormalities.',
    '4': 'You have Trisomy 4p. This disorder is characterized by growth deficiency before and after birth (prenatal and postnatal growth retardation), feeding problems during early infancy, and increased muscle tone (hypertonia) in the first months of life, followed by diminished muscle tone (hypotonia).' ,
    '5': 'You have Trisomy 5p. This disorder is characterized by growth delays after birth, malformations of the head and facial (craniofacial) area, and abnormalities of the hands and feet.',
    '6': 'You have Partial Trisomy 6q. This disorder is characterized by growth delays before and after birth, severe to profound mental retardation, a delay in the acquisition of skills requiring coordination of muscular and mental activity (psychomotor retardation), distinctive malformations of the skull and facial (craniofacial) region, musculoskeletal abnormalities, and/or additional physical features.',
    '7': 'You have Partial Monosomy 7p. This disorder is characterized by growth deficiency, musculoskeletal abnormalities, genital defects, structural malformations of the heart that are present at birth (congenital heart defects), and/or other abnormalities.',
    '8': 'You have Mosaic trisomy 8. This disorder is characterized by brain malformations, highly arched or cleft palate, shortened neck with extra skin folds, long slim body with a narrow chest, shoulders, and pelvis and kidney and cardiac abnormalities.' ,
    '9':  'You have Mosaic Trisomy 9. This disorder is characterized by growth deficiency beginning before birth, failure to grow and gain weight at the expected rate (failure to thrive) during infancy, and low muscle tone (hypotonia).',
    '10': 'You have Distal Trisomy 10q. This disorder is characterized by abnormally slow growth before and after birth, malformations of the head and facial (craniofacial) area, a small nose with turned up nostrils (anteverted nares) and a broad, flat, and/or depressed nasal bridge, a small, bow-shaped mouth with a prominent upper lip,  an unusually small lower jaw, and/or, in some patients, incomplete closure of the roof of the mouth (cleft palate).',
    '11': 'You have Partial Trisomy 11q. This disorder is characterized by growth retardation before and after birth, delayed acquisition of skills requiring the coordination of mental and motor activities (psychomotor retardation), mild to moderate mental retardation, and distinctive craniofacial abnormalities.',
    '12': 'You have Trisomy 12p. This disorder is characterized by macrocephaly (unusually large head), abnormal muscle tone, characteristic facial features, developmental delay and intellectual disability.',
    '13': 'You have Patau syndrome or Trisomy 13. This disorder is characterized by severe intellectual disability and many physical abnormalities, such as congenital heart defects, brain or spinal cord abnormalities, very small or poorly developed eyes (microphthalmia), extra fingers or toes, cleft lip with or without cleft palate, and weak muscle tone (hypotonia).',
    '14': 'You have Mosaic Trisomy 14. This disorder is characterized by rowth delays before birth (intrauterine growth retardation), failure to grow and gain weight at the expected rate (failure to thrive) during infancy, delays in the acquisition of skills requiring the coordination of mental and physical abilities (psychomotor delays), and mental retardation.',
    '15': 'You have Trisomy 15q. This disorder is characterized by developmental delay, intellectual disability, hypotonia (low muscle tone), seizures; high and/or cleft palate (roof of the mouth), scoliosis; slow growth, communication difficulties, behavioral problems, and distinctive facial features.',
    '16': 'You have Trisomy 16. This disorder is characterized by cardiac malformations, hypospadias, two vessel cords, clinodactyly and pulmonary hypoplasia.',
    '17': 'You have Trisomy 17. This disorder is characterized by developmental delays, body asymmetry, slow growth, and cerebellar hypoplasia.',
    '18': "You have Edwards' syndrome or Trisomy 18. This disorder is characterized by slow growth before birth (intrauterine growth retardation), a low birth weight, heart defects and abnormalities of other organs that develop before birth, a small, abnormally shaped head, a small jaw and mouth, and clenched fists with overlapping fingers.",
    '19': 'You have Mosaic Trisomy 19. This disorder is characterized by hydrops, epicanthal fold, hypertelorism, flat nasal bridge, short nose, small mouth, low-set and malformed ears, narrow meati, short neck with excessive skin, short chest, and protuberant abdomen.' ,
    '20': 'You have Trisomy 20. This disorder is characterized by spinal abnormalities (including spinal stenosis, vertebral fusion, and kyphosis), hypotonia (decreased muscle tone), lifelong constipation, sloped shoulders, and significant learning disabilities despite normal intelligence.',
    '21': 'You have Down sydrome or Trisomy 21. This disorder is characterized by a round face, skin fold at inner corner of eye, flattened nose bridge, small, irregular teeth, short stature, heart defects, susceptibility to respiratory infections, Leukemia, Alzheimer’s disease, and a life span shorter than normal.',
    '22': 'You have Mosaic Trisomy 22. This disorder is characterized by growth and developmental delays, asymmetric body development, and congenital heart diseases.
    '23': 'If you have an extra X chromosome, you have Klinefelter’s syndrome. This disorder is characterized by abnormally small tests, sterility, female body characteristics, and subnormal intelligence. If you have an extra Y chromosome, you have XYY syndrome. Individuals with this disorder tend to be taller than average.'
    }
if question == 'XY':
    print('You are biologically male.')
    question2 = input('Do you have an extra copy of any chromosome? ')
    if question2 == 'Yes' or question2 == 'yes':
        question3 = input('On which chromosome do you have an extra copy? ')
        print(data1[question3])

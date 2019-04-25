#Python code that determines the syndrome based on inputted chromosomal abnormalities

name = input('Hello, what is your name? ')
question = input('Hi '+name+', what are your sex chromosomes? ')

data = {
    '1': 'You have Chromosome 1q21.1 duplication syndrome. This disorder is characterized by a large head size (macrocephaly), mild to moderate developmental delay and learning difficulties, autism or autistic-like behavior, heart problems, seizures, and/or and distinctive facial features.'
    '2': 'You have Trisomy 2 mosaicism. This disorder is characterized by intrauterine growth restriction (IUGR), any of various birth defects, distinctive facial features, growth delay, developmental delays, and intellectual disabilities.'
    '3': 'You have Trisomy 3q2. This disorder is characterized by mental retardation, moderate to severe developmental delays, abnormally diminished muscle tone (hypotonia), distinctive abnormalities of the head and facial (craniofacial) area, and/or additional physical abnormalities.'
    '4': 'You have Trisomy 4p. This disorder is characterized by growth deficiency before and after birth (prenatal and postnatal growth retardation), feeding problems during early infancy, and increased muscle tone (hypertonia) in the first months of life, followed by diminished muscle tone (hypotonia).' 
    '5': 'You have Trisomy 5p. This disorder is characterized by growth delays after birth, malformations of the head and facial (craniofacial) area, and abnormalities of the hands and feet.'
    '6': 'You have Partial Trisomy 6q. This disorder is characterized by growth delays before and after birth, severe to profound mental retardation, a delay in the acquisition of skills requiring coordination of muscular and mental activity (psychomotor retardation), distinctive malformations of the skull and facial (craniofacial) region, musculoskeletal abnormalities, and/or additional physical features.'
    '7': 'You have Partial Monosomy 7p. This disorder is characterized by growth deficiency, musculoskeletal abnormalities, genital defects, structural malformations of the heart that are present at birth (congenital heart defects), and/or other abnormalities.'
    '8': 'You have Mosaic trisomy 8. This disorder is characterized by brain malformations, highly arched or cleft palate, shortened neck with extra skin folds, long slim body with a narrow chest, shoulders, and pelvis and kidney and cardiac abnormalities. 



    '9':  '
    '10': '
    '11': '
    '12': '
    '13': '
    '14': ' 
    '15': '  
    '16': '
    '17': '
    '18': '
    '19': '
    '20': ' 
    '21': '
    '22': '
    '23': 'You have an extra X chromosome. However, you may notice there is not much different about you from the outside. The reason is females with an extra X chromosome cannot be distinguished from XX females except by karyotype. ',
    




if question == 'XX':
    print('You are biologically female.')
    question2 = input('Do you have an extra copy of any chromosome? ')
    if question2 == 'Yes' or question2 == 'yes':
        question3 = input('On which chromosome do you have an extra copy? ')
        print(data[question3])
        
if question == 'XY':
    print('You are biologically male.')
    question2 = input('Do you have an extra copy of any chromosome? ')
    if question2 == 'Yes' or question2 == 'yes':
        question3 = input('On which chromosome do you have an extra copy? ')
        print(data[question3])

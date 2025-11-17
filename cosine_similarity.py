from nltk.tokenize import word_tokenize

docs=[]

docs.append("I am by birth a Genevese, and my family is one of the most distinguished of that republic. My ancestors had been for many years counsellors and syndics, and my father had filled several public situations with honour and reputation. He was respected by all who knew him for his integrity and indefatigable attention to public business. He passed his younger days perpetually occupied by the affairs of his country; a variety of circumstances had prevented his marrying early, nor was it until the decline of life that he became a husband and the father of a family. As the circumstances of his marriage illustrate his character, I cannot refrain from relating them. One of his most intimate friends was a merchant who, from a flourishing state, fell, through numerous mischances, into poverty. This man, whose name was Beaufort, was of a proud and unbending disposition and could not bear to live in poverty and oblivion in the same country where he had formerly been distinguished for his rank and magnificence. Having paid his debts, therefore, in the most honourable manner, he retreated with his daughter to the town of Lucerne, where he lived unknown and in wretchedness. My father loved Beaufort with the truest friendship and was deeply grieved by his retreat in these unfortunate circumstances. He bitterly deplored the false pride which led his friend to a conduct so little worthy of the affection that united them. He lost no time in endeavouring to seek him out, with the hope of persuading him to begin the world again through his credit and assistance. Beaufort had taken effectual measures to conceal himself, and it was ten months before my father discovered his abode. Overjoyed at this discovery, he hastened to the house, which was situated in a mean street near the Reuss. But when he entered, misery and despair alone welcomed him. Beaufort had saved but a very small sum of money from the wreck of his fortunes, but it was sufficient to provide him with sustenance for some months, and in the meantime he hoped to procure some respectable employment in a merchant’s house. The interval was, consequently, spent in inaction; his grief only became more deep and rankling when he had leisure for reflection, and at length it took so fast hold of his mind that at the end of three months he lay on a bed of sickness, incapable of any exertion. His daughter attended him with the greatest tenderness, but she saw with despair that their little fund was rapidly decreasing and that there was no other prospect of support. But Caroline Beaufort possessed a mind of an uncommon mould, and her courage rose to support her in her adversity. She procured plain work; she plaited straw and by various means contrived to earn a pittance scarcely sufficient to support life. Several months passed in this manner. Her father grew worse; her time was more entirely occupied in attending him; her means of subsistence decreased; and in the tenth month her father died in her arms, leaving her an orphan and a beggar. This last blow overcame her, and she knelt by Beaufort’s coffin weeping bitterly, when my father entered the chamber. He came like a protecting spirit to the poor girl, who committed herself to his care; and after the interment of his friend he conducted her to Geneva and placed her under the protection of a relation. Two years after this event Caroline became his wife.")
docs.append("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only. There were a king with a large jaw and a queen with a plain face, on the throne of England; there were a king with a large jaw and a queen with a fair face, on the throne of France. In both countries it was clearer than crystal to the lords of the State preserves of loaves and fishes, that things in general were settled for ever. It was the year of Our Lord one thousand seven hundred and seventy-five. Spiritual revelations were conceded to England at that favoured period, as at this. Mrs. Southcott had recently attained her five-and-twentieth blessed birthday, of whom a prophetic private in the Life Guards had heralded the sublime appearance by announcing that arrangements were made for the swallowing up of London and Westminster. Even the Cock-lane ghost had been laid only a round dozen of years, after rapping out its messages, as the spirits of this very year last past (supernaturally deficient in originality) rapped out theirs. Mere messages in the earthly order of events had lately come to the English Crown and People, from a congress of British subjects in America: which, strange to relate, have proved more important to the human race than any communications yet received through any of the chickens of the Cock-lane brood.")
docs.append("‘My uncle, what a worthy man, Falling ill like that, and dying; It summons up respect, one can Admire it, as if he were trying. Let us all follow his example! But, God, what tedium to sample That sitting by the bed all day, All night, barely a foot away! And the hypocrisy, demeaning, Of cosseting one who’s half alive; Puffing the pillows, you contrive To bring his medicine unsmiling, Thinking with a mournful sigh, 'Why the devil can’t you die?’. Such our young dog’s meditation, As his horses plough the dust, Inheriting, as sole relation, By the will of Zeus the Just. Friends of Ruslan and Ludmila, Here without an ounce of bother, Meet my hero of romance, Before you, let him now advance. Eugene Onegin, born and raised There beside the Neva’s shore, Where you too were nourished or Found your fame, perhaps amazed, There I too strolled to and fro: Though the North affects me so.")


def create_bags(docs):
    bags=[]
    for doc in docs:
        bags.append(word_tokenize(doc))
    bag0, bag1, bag2 = bags
    return bag0, bag1, bag2

def dict_count(bag):
    dict_of_counts = {}
    for item in bag:
        dict_of_counts[item] = bag.count(item)
    return dict_of_counts

def make_matrix(list_of_dicts):
    allfeatures={}    
    for docdict in list_of_dicts:
        for feat in docdict.keys():
            allfeatures[feat]=1
    
    dimensions=list(allfeatures.keys())
    #don't strictly need to sort it - but it is good practise to make sure it is reproducible
    sorted(dimensions)
    
    matrix=[]
    #each row in the matrix will be one of the dimensions
    for dimension in dimensions:
        row=[]
        #look up the appropriate value for each document
        for docdict in list_of_dicts:
            row.append(docdict.get(dimension,0)) #this will append the document's value if present, 0 otherwise
        matrix.append(row)
        
        
    return matrix

def transpose(matrix):
    transposed=[]
    for i in range(0,len(matrix[0])):
        transposed.append([row[i] for row in matrix])
        
    return transposed

def naiveCosine(a,b):
    num = 0
    d1 = 0
    d2 = 0
    for i in range (len(a)):
        num += a[i]*b[i]
        d1 += a[i]*a[i]
        d2 += b[i]*b[i]
    return num / (d1*d2)**0.5

def cosine_similarity(bags):
    dictionary_cosine = {}
    n = len(bags)

    for i in range(n):
        for j in range(i + 1, n):
            c = naiveCosine(bags[i], bags[j])
            if c != 1:
                dictionary_cosine[(i + 1, j + 1)] = c

    return dictionary_cosine

def main():
    """Prints a sorted dictionary of the cosine similarity between the documents"""
    bag0, bag1, bag2 = create_bags(docs)

    docdicts = [dict_count(bag0), dict_count(bag1), dict_count(bag2)]

    docdicts = make_matrix(docdicts)
    docdicts = transpose(docdicts)

    cosine_dict = cosine_similarity(docdicts)

    print(dict(sorted(cosine_dict.items(), key=lambda item: item[1])))

if __name__ == "__main__":
    main()
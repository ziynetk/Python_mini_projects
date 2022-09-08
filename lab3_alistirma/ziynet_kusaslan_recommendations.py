#recommendations.py
import math

# Yuksek benzerlik 1, dusuk benzerlik 0
# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    """ Verilen sozluk icindeki p1 ve p2 kisisi icin Pearson korelasyon skorunu hesaplar. 

        Args:
            @prefs: Degerlerin oldugu sozluk
            @p1: Birinci kisinin ismi, 
            @p2: Ikinci kisinin ismi

        Returns:
            0-1 arasinda benzerlik olcutu (0 hic benzemiyor).
    """
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1

    # if they are no ratings in common, return 0
    if len(si) == 0: return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si]) # sum(xi)
    sum2 = sum([prefs[p2][it] for it in si]) # sum(yi)

    #x_mean = sum1/n
    #y_mean = sum2/n

    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si]) # sum(xi*xi)
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si]) # sum(yi*yi)

    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si]) # sum(x*y)

    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2 / n)
    den = math.sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den

    return r

def sim_distance(prefs, person1, person2):
    """ Verilen sozluk icindeki p1 ve p2 kisisi icin Oklit mesafe skorunu hesaplar. 

        Args:
            @prefs: Degerlerin oldugu sozluk
            @p1: Birinci kisinin ismi, 
            @p2: Ikinci kisinin ismi

        Returns:
            0-1 arasinda benzerlik olcutu (0 hic benzemiyor).
    """

    # Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]: 
            si[item]=1

    # if they have no ratings in common, return 0
    if len(si)==0: 
        return 0

    # Add up the squares of all the differences
    sum_of_squares=sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in si])
    oklid = math.sqrt(sum_of_squares)
    #print(oklid)

    return 1/(1+oklid)

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    ''' Pref sözlüğünden person için en iyi eşleşmeleri döndürür.'''
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores

def getRecommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person: continue
        sim = similarity(prefs, person, other)
        # ignore scores of zero or lower
        if sim <= 0: continue
        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings

#1.SORU JACCARD
def sim_jaccard(prefs,person1, person2):
    kesisim = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            kesisim[item] = 1
    birlesim = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            birlesim[item] = 1
        if item in prefs[person1]:
            birlesim[item] = 1

    return float(len(kesisim) / len(birlesim))

#3.SORU COSINE BENZERLİĞİ
def sim_cosine(prefs,person1, person2):
    #pay kısmının hesaplanması nokta çarpımları
    pay = sum(a * b for a, b in zip(prefs[person1].values(), prefs[person2].values()))
    #paydanın hesaplanması için tek tek normlarını buluyoruz
    normPerson1 = math.sqrt(sum(x * x for x in prefs[person1].values()))
    normPerson2 = math.sqrt(sum(x * x for x in prefs[person2].values()))
    return (pay / (normPerson1 * normPerson2))




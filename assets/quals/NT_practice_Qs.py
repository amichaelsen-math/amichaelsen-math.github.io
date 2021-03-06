'''
NT_practice_Qs.py contains lists of practice qualifying exam questions 
from Neukirch's Algebraic Number Theory Chapters 1 & 2 as well as Class Field Theory
along with a function that randomly selects a desired number of questions 
from specified chapters/topics

Author: Anya Michaelsen 
'''
import random
questions_ch1 = [ #Global Number Theory - Neukirch's 'Algebraic Number Theory' Chapter 1 Sections 1-10
    'What is integrality and why is it important? Give examples and non-examples.',
    'What is the ideal class group? class number? How do you show finiteness?',
    'Give an example of a number field with nontrivial class group? How do you compute it?',
    'Give an example of a ring of integers without unique factorization? How do you know?',
    'What is the Minkowski Bound? How is it derived?',
    'Compute the class group of Q(sqrt(-23))',
    'What does Dirichlet\'s unit theorem say? Sketch the proof. Do you know any examples of fundamental units?',
    'Let K be the splitting field of x^8+1, what is the rank of the unit group of O_K?',
    'Consider Q(sqrt(-5)), which primes ramify, split, or remain inert?',
    'Let K be the splitting field of x^4+1, say all you can about K (Galois group, ramified primes, etc)',
    'Let K/Q be a finite Galois extension with group G, show that the inertia subgroups generate G',
    'What are inertia and decomposition groups? How do they encode ramification information?',
    'Let K=Q(\zeta_p) what can you say about quadratic subfields of K?',
    'What is a Dedekind domain? What are some examples and nonexamples?',
    'What are some tests for irreducibility of a polynomial?',
    'What are the units of a (finite) cyclic group?',
    'What does it mean to be integrally closed? What are some sufficient conditions?',
    'How do you prove that O_K is a finitely generated Z-module?',
    'What is the determinant of a field extension? How can it be defined more generally? How does it relate to the discriminant of a polynomial?',
    'Why do we look at ideals and the ideal class group? How do you prove that the ideals have this property?',
    'State quadratic reciprocity and the supplememtal laws',
    'What can you say about how primes split/ramify in extensions of number fields? (don\'t forget Dedekind-Kummer!)',
    'What is O_K for a quadratic number field Q(sqrt(D))? What is the discriminant?',
    'How do lattices relate to number fields? What is the embedding?',
    'What is the decomposition group of L/K for p? What is the inertia subgroup? Show that I_p = 1 if and only if L/K is unramified.',
    'Let OK be a ring of integers. What other Dedekind domains lie inside OK? What other domains can we construct from OK?' # hint: sub rings of integers and localizaions (DVRs)
]

questions_ch2 = [ #Local Number Theory - Neukirch's 'Algebraic Number Theory' Chapter 2 Sections 1-8 
    'State a version of Hensel\'s Lemma. What are some generalizations?',
    'What are the p-adic numbers/integers? What is the topology of Q_p*?',
    'How do the Galois groups of global/local extensions relate?',
    'What are local fields? Show that all ideals are powers of the maximal ideal.',
    'Let L/K be an extension of local fields. What is the inertia subgroup? What does it mean to have an extension of valuations?',
    'What is the structure of (Z/p^kZ)^*? What about Z_p^*?',
    'What are the roots of unity in Q_p^*?',
    'What are the roots of unity in Q_2*? Q_3*?',
    'Let K be Q adjoin a root of x^n-2 (n>=2). What is [K:Q]? How many ways can you extend the archimedean valuation on Q? What about the 2-adic valuation? What is the unit group of OK?' #milne's ANT Practice Exam Q2
]

questions_cft = [ #Class Field Theory Questions
    'What is a statement of Artin Reciprocity? How does it extend Quadratic reciprocity?',
    'Prove that if almost all primes split completely in L/K (not necessarily Galois) then L=K.', #hint: Chebotarev density theorem 
    'What are the statements of (local/global) class field theory?',
    'Take a=(1,..., pi,...1) in A_K (pi in the pth place), and an unramified at p extension L/K. Where does a get sent in Gal(L/K)?',
    'What is the frobenius element in Gal(L/K) for p? If L/K is unramified at p, how do you lift from reisdue fields?',
    'What are the adeles? ideles? What is the embedding K* -> I_K? What is the norm map?',
    'What is a statement of Chebotarev density?',
    'How many quadratic extensions of Q_2 are there? Q_5?',
    'Use CFT to give an enumeration of the quadratic extensions of Q.',
    'Given the existence and properties of local artin maps, what needs to be true for these to combine to give a global artin map?', #trivial on principal embedding, only finitely many have decomp
    'In the case of K=Q, how does the global artin map simplify? (i.e. rewrite both C_Q and Gal(Q^ab/Q). What is Q^ab? How do you know?'
]



def pick_NT_questions(n=5, ch1=True, ch2=True, cft=True):
    print("")
    questions = []
    if(ch1):
        questions += questions_ch1 
    if(ch2):
        questions += questions_ch2 
    if(cft):
        questions += questions_cft
    selected_qs = random.sample(questions,n)
    for i, q in enumerate(selected_qs):
     print(str(i+1)+". "+q+"\n")

def chapter_one(n):
    pick_NT_questions(n, ch1=True, ch2=False, cft=False)

def chapter_two(n):
    pick_NT_questions(n, ch1=False, ch2=True, cft=False)

def class_field_theory(n):
    pick_NT_questions(n, ch1=False, ch2=False, cft=True)


pick_NT_questions(10)
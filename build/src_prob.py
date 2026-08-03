# -*- coding: utf-8 -*-
"""Probability Essentials (KSE) — 16 'Preparation lecture materials' in 5 blocks."""
REL = "source/Syllabus_Probability_essentials.pdf"; D = "probability"

M = {
 1: "Preparation lecture materials 1. Logical propositions, true/false propositions.",
 2: "Preparation lecture materials 2. Logical operations, truth tables.",
 3: "Preparation lecture materials 3. Building negations to claims.",
 4: "Sets and subsets, set operations, Euler",
 5: "Preparation lecture materials 5. The Number of Elements in a Finite Set.",
 6: "Cartesian product, multiplication and addition",
 7: "Preparation lecture materials 7. Permutations and Combinations.",
 8: "Preparation lecture materials 8. Event space, events.",
 9: "Preparation lecture materials 9. Probability definition. Rules of probability.",
 10: "Usage of combinatorics in probability word",
 11: "Preparation lecture materials 11. Conditional probability and independent events.",
 12: "Preparation lecture materials 12. Total probability law (chain rule).",
 13: "Preparation lecture materials 13. A posteriori probability, Bayes’ rule.",
 15: "Preparation lecture materials 15. Random distributions. Expected value.",
 16: "Preparation lecture materials 16. Random distributions. Variance and standard",
}
B = {
 1: "Block 1. Basics of logic and set theory",
 2: "Block 2. Set theory and combinatorics",
 3: "Block 3. Probability, rules of probability",
 4: "Block 4. Conditional probability, independent events, Bayes’ rule",
 5: "Block 5. Random variables. Random distributions and their characteristics",
}

def c(slug, name, kind, diff, definition, aliases, quotes):
    return dict(slug=slug, name=name, kind=kind, difficulty=diff, domain=D,
                definition=definition, aliases=aliases,
                occurrences=[{"rel_path": REL, "role": r, "quote": q, "confidence": 0.9}
                             for r, q in quotes])

UNITS = {
 "PROB-P01": (1, 1, "Materials 1. Logical propositions", [
   c("logical-proposition","Logical Proposition","definition",1,"A statement that is definitely either true or false, the atom of formal reasoning.",["true/false propositions"],[("introduced",M[1])]),
 ]),
 "PROB-P02": (1, 2, "Materials 2. Logical operations and truth tables", [
   c("logical-operations","Logical Operations","method",1,"Negation, conjunction, disjunction and implication, which combine propositions into compound statements.",[],[("introduced",M[2])]),
   c("truth-table","Truth Table","tool",1,"An exhaustive table of a compound statement's value for every assignment of its parts.",["truth tables"],[("introduced",M[2])]),
 ]),
 "PROB-P03": (1, 3, "Materials 3. Negations of claims", [
   c("negation-of-claim","Building Negations to Claims","method",2,"Turning a statement, including quantified ones, into its correct denial — the skill behind complementary events.",["negation"],[("introduced",M[3])]),
 ]),
 "PROB-P04": (1, 4, "Materials 4. Sets and set operations", [
   c("set","Set","definition",1,"A collection of distinct objects considered as one whole.",["sets"],[("introduced",M[4]),("defined",B[1])]),
   c("subset","Subset","definition",1,"A set all of whose elements belong to another set.",["subsets"],[("introduced",M[4])]),
   c("set-operations","Set Operations","method",2,"Union, intersection, difference and complement, the operations mirrored later by operations on events.",[],[("introduced",M[4])]),
   c("euler-diagram","Euler Diagram","tool",1,"A picture of sets as regions, used to reason about their overlaps.",["Venn diagram","Euler diagrams"],[("introduced",M[4])]),
 ]),
 "PROB-P05": (2, 1, "Materials 5. Cardinality of a finite set", [
   c("cardinality-of-finite-set","The Number of Elements in a Finite Set","principle",2,"Counting a finite set, including the inclusion–exclusion correction for overlapping parts.",["inclusion-exclusion","cardinality"],[("introduced",M[5])]),
 ]),
 "PROB-P06": (2, 2, "Materials 6. Cartesian product and counting rules", [
   c("cartesian-product","Cartesian Product","definition",2,"The set of all ordered pairs drawn from two sets, the formal model of independent choices.",[],[("introduced",M[6]),("defined",B[2])]),
   c("multiplication-rule","Multiplication Rule","principle",2,"When choices are made in sequence, the number of outcomes is the product of the counts.",[],[("introduced",M[6])]),
   c("addition-rule","Addition Rule","principle",2,"When alternatives are mutually exclusive, the number of outcomes is the sum of the counts.",[],[("introduced",M[6])]),
 ]),
 "PROB-P07": (2, 3, "Materials 7. Permutations and combinations", [
   c("permutation","Permutation","definition",3,"An arrangement of objects where order matters.",["permutations"],[("introduced",M[7])]),
   c("combination","Combination","definition",3,"A selection of objects where order does not matter; the binomial coefficient counts them.",["combinations","binomial coefficient"],[("introduced",M[7])]),
 ]),
 "PROB-P08": (3, 1, "Materials 8. Event space and events", [
   c("event-space","Event Space","definition",2,"The set of all possible outcomes of an experiment, the universe in which probability is defined.",["sample space"],[("introduced",M[8]),("defined",B[3])]),
   c("event","Event","definition",2,"A subset of the event space, so that operations on events are operations on sets.",["events"],[("introduced",M[8])]),
 ]),
 "PROB-P09": (3, 2, "Materials 9. Definition and rules of probability", [
   c("probability","Probability","definition",2,"A number between 0 and 1 assigned to an event, measuring how likely it is.",["probability definition"],[("introduced",M[9])]),
   c("probability-rules","Rules of Probability","principle",3,"The axioms and their consequences: complement, addition for unions, monotonicity.",[],[("introduced",M[9])]),
 ]),
 "PROB-P10": (3, 3, "Materials 10. Combinatorics in probability problems", [
   c("combinatorial-probability","Combinatorics in Probability Problems","method",3,"Computing probabilities of equally likely outcomes by counting favourable and total cases.",[],[("introduced",M[10])]),
 ]),
 "PROB-P11": (4, 1, "Materials 11. Conditional probability and independence", [
   c("conditional-probability","Conditional Probability","definition",3,"The probability of an event given that another has occurred, obtained by restricting the event space.",[],[("introduced",M[11]),("defined",B[4])]),
   c("independent-events","Independent Events","definition",3,"Events where knowing one occurred does not change the probability of the other.",[],[("introduced",M[11])]),
 ]),
 "PROB-P12": (4, 2, "Materials 12. Total probability law", [
   c("total-probability-law","Total Probability Law","principle",4,"Decomposing an event's probability across a partition of the event space; the chain rule of probability.",["chain rule"],[("introduced",M[12])]),
 ]),
 "PROB-P13": (4, 3, "Materials 13–14. Bayes' rule", [
   c("posterior-probability","A Posteriori Probability","definition",4,"The updated probability of a hypothesis after evidence has been observed.",["a posteriori probability"],[("introduced",M[13])]),
   c("bayes-rule","Bayes' Rule","principle",4,"The formula inverting a conditional probability, turning likelihood and prior into posterior.",["Bayes’ rule","Bayes theorem"],[("introduced",M[13]),("defined",B[4])]),
 ]),
 "PROB-P15": (5, 1, "Materials 15. Random variables and expected value", [
   c("random-variable","Random Variable","definition",3,"A numerical quantity whose value is determined by the outcome of a random experiment.",["random variables"],[("introduced",B[5])]),
   c("random-distribution","Random Distribution","definition",3,"The assignment of probabilities to the values a random variable can take.",["random distributions","probability distribution"],[("introduced",M[15])]),
   c("expected-value","Expected Value","metric",3,"The probability-weighted average of a random variable, its long-run mean.",["mean","expectation"],[("introduced",M[15])]),
 ]),
 "PROB-P16": (5, 2, "Materials 16. Variance and standard deviation", [
   c("variance","Variance","metric",3,"The expected squared deviation from the mean, measuring spread.",[],[("introduced",M[16])]),
   c("standard-deviation","Standard Deviation","metric",3,"The square root of the variance, expressing spread in the units of the variable.",[],[("introduced",M[16])]),
 ]),
}

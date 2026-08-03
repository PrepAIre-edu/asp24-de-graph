# -*- coding: utf-8 -*-
"""Calculus (KSE) — 15 lectures across 4 topics. Quotes are the syllabus's own
lecture-content lines, which name every concept explicitly."""
REL = "source/Syllabus_Calculus.pdf"; D = "calculus"

L = {
 1: "Sequences. Examples. Limit of sequence. Properties of convergent sequences. Number e",
 2: "Limit of a function at a point. Cauchy (ε–δ) definition and Heine (sequence) definition. Properties of limits. One-sided",
 3: "Big-O and little-o notation. Special limits",
 4: "Properties of functions continuous on a closed interval.",
 4.1: "Cauchy’s intermediate value theorem. Weierstrass’s theorem.",
 5: "Definition of the derivative. Motivation. Differentiation rules. Properties.",
 6: "Differentiable functions. Their properties. The theorems of Rolle, Lagrange, and Cauchy.",
 7: "Differential of a function. Higher-order derivatives.",
 8: "Taylor’s formula. L’Hôpital’s rule.",
 9: "Convexity. The second derivative test. Graphing functions.",
 10: "Antiderivative and indefinite integral. Substitution.",
 11: "Integrating by parts",
 12: "Definite integral. Properties of the definite integral. Mean value theorem for integrals. Newton–Leibniz formula.",
 13: "Formulas of substitution and integration by parts. Some applications of the definite integral. Improper integrals.",
 14: "Series. Convergence of series. Examples. Tests for convergence of numerical series.",
 15: "Power series. Taylor series. Maclaurin series. Domains of convergence.",
}
TOPIC = {1: "Topic 1. Limits", 2: "Topic 2. Derivatives", 3: "Topic 3. Integral", 4: "Topic 4. Series"}

# unit_id -> (module=topic, ordinal, title, [concepts])
def c(slug, name, kind, diff, definition, aliases, quotes):
    return dict(slug=slug, name=name, kind=kind, difficulty=diff, domain=D,
                definition=definition, aliases=aliases,
                occurrences=[{"rel_path": REL, "role": r, "quote": q, "confidence": 0.9}
                             for r, q in quotes])

UNITS = {
 "CALC-L01": (1, 1, "Lecture 1. Sequences and their limits", [
   c("sequence","Sequence","definition",1,"An ordered infinite list of numbers indexed by the natural numbers.",["sequences"],[("introduced",L[1])]),
   c("limit-of-sequence","Limit of a Sequence","definition",2,"The value a sequence approaches arbitrarily closely as the index grows without bound.",["sequence limit"],[("introduced",L[1])]),
   c("convergent-sequence","Convergent Sequence","definition",2,"A sequence that has a finite limit; such sequences are bounded and their limits respect arithmetic.",["properties of convergent sequences"],[("introduced",L[1])]),
   c("number-e","The Number e","definition",2,"The limit of (1+1/n)^n, the base of the natural exponential and logarithm.",["Euler's number"],[("introduced",L[1])]),
 ]),
 "CALC-L02": (1, 2, "Lecture 2. Limit of a function", [
   c("limit-of-function","Limit of a Function at a Point","definition",2,"The value a function approaches as its argument approaches a given point, independently of the value at that point.",["function limit"],[("introduced",L[2])]),
   c("epsilon-delta-definition","Cauchy (ε–δ) Definition of a Limit","definition",3,"The formal definition: for every ε there is a δ such that arguments within δ of the point map to values within ε of the limit.",["Cauchy definition","epsilon-delta"],[("introduced",L[2])]),
   c("heine-definition","Heine (Sequential) Definition of a Limit","definition",3,"An equivalent definition of a function limit stated through the limits of all sequences approaching the point.",["sequence definition of a limit"],[("introduced",L[2])]),
   c("one-sided-limit","One-Sided Limit","definition",2,"The limit taken as the argument approaches a point from only the left or only the right.",["one-sided limits"],[("introduced",L[2])]),
 ]),
 "CALC-L03": (1, 3, "Lecture 3. Asymptotic notation and special limits", [
   c("big-o-notation","Big-O Notation","definition",3,"A notation bounding a function's growth from above up to a constant factor, used to compare rates of change.",["Big-O"],[("introduced",L[3])]),
   c("little-o-notation","Little-o Notation","definition",3,"A notation stating that one function is asymptotically negligible relative to another.",["little-o"],[("introduced",L[3])]),
   c("special-limits","Special Limits","principle",2,"The small catalogue of standard limits that serve as building blocks for evaluating harder ones.",[],[("introduced",L[3])]),
 ]),
 "CALC-L04": (1, 4, "Lecture 4. Continuity on a closed interval", [
   c("continuity","Continuity on a Closed Interval","definition",3,"A function is continuous on a closed interval when small changes of argument produce small changes of value throughout it, which guarantees strong global properties.",["continuous function"],[("introduced",L[4])]),
   c("intermediate-value-theorem","Cauchy's Intermediate Value Theorem","principle",3,"A function continuous on a closed interval attains every value between its endpoint values.",["IVT"],[("introduced",L[4.1])]),
   c("weierstrass-theorem","Weierstrass's Theorem","principle",3,"A function continuous on a closed bounded interval is bounded and attains a maximum and a minimum on it.",["extreme value theorem"],[("introduced",L[4.1])]),
 ]),
 "CALC-L05": (2, 1, "Lecture 5. The derivative", [
   c("derivative","Derivative","definition",2,"The instantaneous rate of change of a function, defined as the limit of its difference quotient.",["derivatives"],[("introduced",L[5]),("defined",TOPIC[2])]),
   c("differentiation-rules","Differentiation Rules","method",2,"The algebraic rules — sum, product, quotient and chain — that let derivatives be computed without returning to the limit.",["chain rule","product rule"],[("introduced",L[5])]),
 ]),
 "CALC-L06": (2, 2, "Lecture 6. Mean value theorems", [
   c("differentiable-function","Differentiable Function","definition",3,"A function possessing a derivative at every point of an interval; differentiability implies continuity.",["differentiable functions"],[("introduced",L[6])]),
   c("rolles-theorem","Rolle's Theorem","principle",3,"A function continuous on a closed interval, differentiable inside it and equal at the endpoints has a stationary point strictly inside.",[],[("introduced",L[6])]),
   c("lagrange-mean-value-theorem","Lagrange Mean Value Theorem","principle",3,"On any interval a differentiable function has a point whose derivative equals the average rate of change across the interval.",["mean value theorem"],[("introduced",L[6])]),
   c("cauchy-mean-value-theorem","Cauchy Mean Value Theorem","principle",4,"A two-function generalisation of the mean value theorem, the basis for L'Hôpital's rule.",[],[("introduced",L[6])]),
 ]),
 "CALC-L07": (2, 3, "Lecture 7. Differentials and higher derivatives", [
   c("differential","Differential of a Function","definition",3,"The linear part of a function's increment, the formal expression of local linear approximation.",[],[("introduced",L[7])]),
   c("higher-order-derivative","Higher-Order Derivative","definition",3,"The result of differentiating repeatedly; the second derivative measures curvature.",["second derivative"],[("introduced",L[7])]),
 ]),
 "CALC-L08": (2, 4, "Lecture 8. Taylor's formula and L'Hôpital's rule", [
   c("taylors-formula","Taylor's Formula","principle",4,"An approximation of a smooth function near a point by a polynomial built from its derivatives, with a controlled remainder.",["Taylor expansion"],[("introduced",L[8])]),
   c("lhopitals-rule","L'Hôpital's Rule","method",3,"A technique for evaluating indeterminate limits by differentiating numerator and denominator separately.",[],[("introduced",L[8])]),
 ]),
 "CALC-L09": (2, 5, "Lecture 9. Convexity and curve sketching", [
   c("convexity","Convexity","definition",3,"A function is convex when its graph lies below its chords; convexity is what makes minimisation well behaved.",["concavity"],[("introduced",L[9])]),
   c("second-derivative-test","Second Derivative Test","method",3,"Classifying a stationary point as a minimum or maximum by the sign of the second derivative there.",[],[("introduced",L[9])]),
   c("function-graphing","Graphing Functions","method",2,"Assembling limits, derivatives and convexity into a full qualitative picture of a function's graph.",["curve sketching"],[("introduced",L[9])]),
 ]),
 "CALC-L10": (3, 1, "Lecture 10. Antiderivative and substitution", [
   c("antiderivative","Antiderivative","definition",3,"A function whose derivative is the given function; differentiation run backwards.",["primitive function"],[("introduced",L[10]),("defined",TOPIC[3])]),
   c("indefinite-integral","Indefinite Integral","definition",3,"The family of all antiderivatives of a function, differing by a constant.",[],[("introduced",L[10])]),
   c("integration-by-substitution","Integration by Substitution","method",3,"Changing variable in an integral so that it matches a known antiderivative; the chain rule reversed.",["substitution"],[("introduced",L[10])]),
 ]),
 "CALC-L11": (3, 2, "Lecture 11. Integration by parts", [
   c("integration-by-parts","Integration by Parts","method",3,"Trading one integral for another using the product rule in reverse.",["integrating by parts"],[("introduced",L[11])]),
 ]),
 "CALC-L12": (3, 3, "Lecture 12. The definite integral", [
   c("definite-integral","Definite Integral","definition",3,"A number attached to a function on an interval, interpretable as signed area under its graph.",[],[("introduced",L[12])]),
   c("mean-value-theorem-for-integrals","Mean Value Theorem for Integrals","principle",4,"A continuous function attains its average value over an interval at some interior point.",[],[("introduced",L[12])]),
   c("newton-leibniz-formula","Newton–Leibniz Formula","principle",3,"The fundamental link: a definite integral equals the increment of any antiderivative across the interval.",["fundamental theorem of calculus"],[("introduced",L[12])]),
 ]),
 "CALC-L13": (3, 4, "Lecture 13. Applications and improper integrals", [
   c("applications-of-definite-integral","Applications of the Definite Integral","method",3,"Using integration to compute areas, volumes, lengths and accumulated quantities.",[],[("introduced",L[13])]),
   c("improper-integral","Improper Integral","definition",4,"An integral over an unbounded interval or of an unbounded function, defined as a limit of ordinary integrals.",["improper integrals"],[("introduced",L[13])]),
 ]),
 "CALC-L14": (4, 1, "Lecture 14. Numerical series", [
   c("series","Series","definition",3,"The formal sum of infinitely many terms, studied through the limit of its partial sums.",["numerical series"],[("introduced",L[14]),("defined",TOPIC[4])]),
   c("convergence-of-series","Convergence of a Series","definition",3,"A series converges when its partial sums approach a finite limit.",[],[("introduced",L[14])]),
   c("convergence-tests","Tests for Convergence","method",4,"The standard criteria — comparison, ratio, root, integral — for deciding convergence without summing.",["convergence criteria"],[("introduced",L[14])]),
 ]),
 "CALC-L15": (4, 2, "Lecture 15. Power and Taylor series", [
   c("power-series","Power Series","definition",4,"A series in powers of the variable, which behaves like a polynomial inside its region of convergence.",[],[("introduced",L[15])]),
   c("taylor-series","Taylor Series","definition",4,"The power series generated by a function's derivatives at a point.",[],[("introduced",L[15])]),
   c("maclaurin-series","Maclaurin Series","definition",4,"The Taylor series taken at zero.",[],[("introduced",L[15])]),
   c("domain-of-convergence","Domain of Convergence","definition",4,"The set of arguments for which a power series converges.",["domains of convergence"],[("introduced",L[15])]),
 ]),
}

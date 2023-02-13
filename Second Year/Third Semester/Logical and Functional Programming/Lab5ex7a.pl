(
    defun eliminate (l n)
        (
            cond
                ((null l) nil)
                ((= n 1) (cdr l))
                (T (cons (car l) (eliminate (cdr l) (- n 1))))
        )
)

(print(eliminate '(1 2 3 4 5 6 7 8) 3))






(defun reversed(l solution)
    (cond
        ((null l) solution)
        (T (reversed (cdr l) (cons (car l) solution)))
    )
)

(defun reverseElements(l)
    (reversed l nil)
)

(defun increase(l)
    (cond
        ((and (equal 9 (car l)) (not (equal nil (cdr l)))) (cons 0 (increase (cdr l))))     
        ((equal 9 (car l)) (cons 0 (cons 1 nil)))
        (t (cons (+ 1 (car l)) (cdr l)))
    )
)

(defun successor(l)
   (reverseElements (increase (reverseElements l))) 
)

(print (successor '(1 9 3 5 9 9)))





(defun contains (l elem)
    (cond
        ((null l) nil)
        ((equal (car l) elem) T)
        (T (contains (cdr l) elem))
    )
)

(defun concat(l1 l2)
    (cond
        ((null l1) l2)
        (T (cons (car l1) (concat (cdr l1) l2)))
    )
)

(defun createLinearList(l)
    (cond
        ((null l) nil)
        ((atom (car l)) (cons (car l) (createLinearList (cdr l))))
        ((listp (car l)) (concat (createLinearList (car l)) (createLinearList (cdr l))))
    )
)

(defun setA(l sol)
    (cond
        ((null l) sol)
        ((contains sol (car l)) (setA (cdr l) sol))
        (T (setA (cdr l) (cons (car l) sol)))
    )
)

(defun createSet(l)
    (setA l nil)
)

(defun solve(l)
    (reverseElements (createSet (createLinearList l)))
)

(print (solve '(1 (2 (1 3 (2 4) 3) 1) (1 4))))
(print (solve '(1 "a" (2 "ab" (1 3 (2 4 A) 3) 1 A) (1 4))))





(defun checkSet(l)
    (cond
        ((null l) T)
        ((contains (cdr l) (car l)) nil)
        (T (checkSet (cdr l)))
    )
)

(print (checkSet '(1 2 2 3 4)))
(print (checkSet '(1 2 3 4)))

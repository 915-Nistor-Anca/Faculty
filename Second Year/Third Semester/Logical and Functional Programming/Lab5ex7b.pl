;Return the level of a node X in a tree of type (1). The level of the root element is 0.

; leftTraversal(l1l2...ln, nbOfNodes, nbOfEdges) = 
; = nil, if n = 0
; = nil, if nbOfNodes = 1 + nbOfEdges
; = {l1} U {l2} U leftTraversal(l3...ln, nbOfNodes + 1, l2 + nbOfEdges), otherwise

(defun leftTraversal (l nbOfNodes nbOfEdges)
  (cond
    ((null l) nil)
    ((= nbOfNodes ( + 1 nbOfEdges)) nil)
    (t (cons (car l) (cons (cadr l) (leftTraversal (cddr l) (+ 1 nbOfNodes) (+ (cadr l) nbOfEdges)))))
  )
)

; rightTraversal(l1l2...ln, nbOfNodes, nbOfEdges) =
; = nil, if n = 0
; = l1l2...ln, if nbOfNodes = 1 + nbOfEdges
; = rightTraversal(l3...ln, nbOfNodes + 1, l2 + nbOfEdges), otherwise


(defun rightTraversal (l nbOfNodes nbOfEdges)
  (cond
    ((null l) nil)
    ((= nbOfNodes (+ 1 nbOfEdges)) l)
    (t (rightTraversal (cddr l) (+ 1 nbOfNodes) (+ (cadr l) nbOfEdges)))
  )
)


;left(l1l2...ln) = 
; = leftTraversal(l3...ln, 0,0)

(defun left(l)
  (leftTraversal (cddr l) 0 0)
)


;right(l1l2...ln) =
; = rightTraversal(l3...ln, 0, 0)

(defun right(l)
  (rightTraversal (cddr l) 0 0)
)


; myAppend(l1l2...ln, p1p2...pm) = 
; = p1p2...pm, if n = 0
; = {l1} U myAppend(l2...ln, p1p2...pm), otherwise

(defun myAppend(l p)
  (cond
    ((null l) p)
    (t (cons (car l) (myAppend (cdr l) p)))
  )
)


; findLevel(l1l2...ln, elem, level) = 
; = 0, if n = 0
; = level, if l1 = elem
; = findLevel(left(l), elem, level + 1) + findLevel(right(l), elem, level + 1)

(defun findLevel(l elem level)
  (cond
    ((null l) 0)
    ((equal (car l) elem) level)
    (t (+ (findLevel (left l) elem (+ 1 level)) (findLevel (right l) elem (+ 1 level))))
  )
)


; nodesFromLevel(l1l2...ln, level, counter) = 
; = nil, if n = 0
; = list(l1), if level = counter
; = myAppend(nodesFromLevel(left(l1l2...ln), level, counter + 1), nodesFromLevel(right(l1l2...ln), level, counter + 1)), otherwise


(defun nodesFromLevel(l level counter)
  (cond
    ((null l) nil)
    ((equal level counter) (list (car l)))
    (t (myAppend (nodesFromLevel (left l) level (+ 1 counter)) (nodesFromLevel (right l) level (+ 1 counter))))
  )
)

; checkExistence(l1l2...ln, elem) = 
; = true, if l1 = elem
; = false, if n = 0
; = checkExistence(l2...ln, elem), otherwise

(defun checkExistence(l elem)
  (cond 
    ((null l) nil)
    ((equal (car l) elem) t)
    (t (checkExistence (cdr l) elem))
  )
)

(defun main(l elem)
  (cond
    ((checkExistence l elem) (nodesFromLevel l (findLevel l elem 0) 0))
    (t nil)
  )
)

(print (main '(A 2 B 0 C 1 D 0 E 0 F 0) 'D))
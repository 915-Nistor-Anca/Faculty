public class KaratsubaAlgorithmSequencialForm {
    public static Polynomial multiply(Polynomial p1, Polynomial p2) {
        if (p1.getDegree() < 2 || p2.getDegree() < 2) {
            return RegularAlgorithmSequencialForm.multiply(p1, p2);
        }

        int len = Math.max(p1.getDegree(), p2.getDegree()) / 2;
        Polynomial a = new Polynomial(p1.getCoefficients().subList(0, len));
        Polynomial b = new Polynomial(p1.getCoefficients().subList(len, p1.getCoefficients().size()));
        Polynomial c = new Polynomial(p2.getCoefficients().subList(0, len));
        Polynomial d = new Polynomial(p2.getCoefficients().subList(len, p2.getCoefficients().size()));

        Polynomial poly1 = multiply(a, c);
        Polynomial poly2 = multiply(PolynomialOperations.add(a, b), PolynomialOperations.add(c, d));
        Polynomial poly3 = multiply(b, d);

        Polynomial r1 = PolynomialOperations.addZeros(poly3, 2 * len);
        Polynomial r2 = PolynomialOperations.addZeros(PolynomialOperations.subtract(PolynomialOperations.subtract(poly2, poly3), poly1), len);
        return PolynomialOperations.add(PolynomialOperations.add(r1, r2), poly1);
    }
}

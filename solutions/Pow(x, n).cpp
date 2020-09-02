class Solution {
private:
    double recursivePow(double x, int n) {
        if (n < 0) {
			int power = n;
			double base = x;

			while (power < -2) {
				if (power % 2) {
					return base * recursivePow(base, power + 1);
				}
				else {
					base = base * base;
					power /= 2;
				}
			}

			return base * base;
		}
		else {
			unsigned int power = n;
			double base = x;

			while (power > 2) {
				if (power % 2) {
					return base * recursivePow(base, power - 1);
				}
				else {
					base = base * base;
					power /= 2;
				}
			}

			return base * base;
		}
	}
    
public:
	double myPow(double x, int n) {
		if (n == 0)
			return 1;
		if (n == 1)
			return x;
        if (n == -1)
            return 1/x;

		if (n < 0) {
			signed int power = n;
			double base = x;

			while (power < -2) {
				if (power % 2) {
					return 1 / (base * recursivePow(base, power + 1));
				}
				else {
					base = base * base;
					power /= 2;
				}
			}

			return 1 / (base * base);
		}
		else {
			unsigned int power = n;
			double base = x;

			while (power > 2) {
				if (power % 2) {
					return base * recursivePow(base, power - 1);
				}
				else {
					base = base * base;
					power /= 2;
				}
			}

			return base * base;
		}
	}
};
class Solution {
private:
	int x = 2;
	int q = 13;

	int power_limit = 15; // bits(type(int))
	vector<int> pows;

	int get32PowerOfX(int _power) {
		int power = _power % power_limit;
		int prev_limit = pows.size();

		if (power == 0)
			return pows[0];
		if (power > pows.size()-1) {
			pows.resize(power + 1);

			for (int i = prev_limit; i <= power; i++) {
				pows[i] = pows[i - 1] << 1;
			}
		}

		return pows[power];
	}

	int calculate_RobinKarpHash(const char* ptr, int index, int size, int m) {
		if (!m)
			return 0;

 		long long hash = (ptr[index] * get32PowerOfX(m)) % q;

		for (int i = 1; i < m; i++) {
			hash += (ptr[(index + i) % size] * get32PowerOfX(m - i)) % q;
		}

		return hash;
	}

	int fast_compare(const char* ptr1, const char* ptr2, int index, int size, int m) {
		if (!m)
			return 0;

		for (int i = 0; i < m; i++) {
			if (ptr1[(index + i) % size] != ptr2[i])
				return false;
		}

		return true;
	}

public:

	Solution() {
		ios_base::sync_with_stdio(false);
		cin.tie(NULL);

		pows.resize(2);
		pows[0] = 1;
		pows[1] = x;
	}

	int repeatedStringMatch(string A, string B) {
		if (!A.size() || !B.size())
			return -1;

		int answer = 0;
		int B_hash = calculate_RobinKarpHash(B.c_str(), 0, B.size(), B.size());
		int ind = 0;
		bool found = false;

		while (ind < A.size()) {
			int A_hash = calculate_RobinKarpHash(A.c_str(), ind, A.size(), B.size());
			if (A_hash == B_hash) {
				if (fast_compare(A.c_str(), B.c_str(), ind, A.size(), B.size()))
					found = true;
				break;
			}

			ind++;
		}

		if (found) {
			int sub_end = ind + B.size();
			if (sub_end <= A.size()) {
				return 1;
			} else {
				return sub_end % A.size() ? sub_end / A.size() + 1 : sub_end / A.size();
			}
		}
		else {
			return -1;
		}
	}
};
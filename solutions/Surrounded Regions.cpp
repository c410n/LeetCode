class Solution {
	int count = 0;
private:
	bool check_adjascent(int starting_y, int starting_x, vector<vector<char>> &board, set<pair<int, int>> &cells) {
		set<pair<int, int>> segment, segment_candidate;
		segment.insert({ starting_y, starting_x });

		cells.insert({ starting_y, starting_x });
		board[starting_y][starting_x] = 'P';

		bool retval = false;

		while (segment.size()) {
			for (auto it = segment.begin(); it != segment.end(); it++) {
				int y = it->first, x = it->second;

				if (y == 0 || x == 0 || y == board.size() - 1 || x == board[0].size() - 1)
					retval |= true;

				// y + 1
				if (y + 1 < board.size() && board[y + 1][x] == 'O') {
					board[y + 1][x] = 'P';

					segment_candidate.insert({ y + 1,x });
					cells.insert({ y + 1, x });
				}

				// x + 1
				if (x + 1 < board[0].size() && board[y][x + 1] == 'O') {
					board[y][x + 1] = 'P';

					segment_candidate.insert({ y,x + 1 });
					cells.insert({ y, x + 1 });
				}


				// y - 1
				if (y > 0 && board[y - 1][x] == 'O') {
					board[y - 1][x] = 'P';

					segment_candidate.insert({ y - 1,x });
					cells.insert({ y - 1, x });
				}

				// x - 1                
				if (x > 0 && board[y][x - 1] == 'O') {
					board[y][x - 1] = 'P';

					segment_candidate.insert({ y,x - 1 });
					cells.insert({ y, x - 1 });
				}
			}

			segment = segment_candidate;
			segment_candidate.clear();
		}

		return retval;
	}

public:

	void solve(vector<vector<char>>& board) {
		if (board.size() < 3)
			return;

		set<pair<int, int>> cells;
		for (int y = 1; y < board.size() - 1; y++) {
			for (int x = 1; x < board[0].size() - 1; x++) {
				if (board[y][x] == 'O')
					if (!check_adjascent(y, x, board, cells)) {
						std::for_each(cells.begin(), cells.end(),
							[&](auto param)
						{
							board[param.first][param.second] = 'X';
						}
						);
					}
					else {
						std::for_each(cells.begin(), cells.end(),
							[&](auto param)
						{
							board[param.first][param.second] = 'O';
						}
						);
					}

					cells.clear();
			}
		}
	}
};
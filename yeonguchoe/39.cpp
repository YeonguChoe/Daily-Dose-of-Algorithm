void backtrack(int current_sum, int goal, int current_start_of_candidate,
  vector < int > & combination, vector < int > & candidate,
  vector < vector < int >> & result) {
  // 합이 정답에 도달하면, 해당 조합을 답에 추가
  if (current_sum == goal) {
    result.push_back(combination);
    return;
  }
  // 합이 정답을 넘어서면, 더이상 들어가지 않음.
  if (current_sum > goal) {
    return;
  }
  // candidate을 combination에 붙였다가 뗏다가 하면서, 함수 실행
  for (int i = current_start_of_candidate; i < candidate.size(); ++i) {
    combination.push_back(candidate[i]);
    backtrack(current_sum + candidate[i], goal, i, combination,
      candidate, result);
    combination.pop_back();
  }
}
vector < vector < int >> combinationSum(vector < int > & candidates, int target) {
  vector < vector < int >> result;
  vector < int > combination;
  backtrack(0, target, 0, combination, candidates, result);
  return result;
}

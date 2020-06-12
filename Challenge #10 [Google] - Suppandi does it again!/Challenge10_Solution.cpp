#include<bits/stdc++.h>

#define int int64_t

using namespace std; 

string rotateleft(string s) {

  if(s.size() == 1) return s;

  else return s.substr(1 , s.length()-1) + s[0];

}

 

string rotateright(string s) {

  if(s.size() == 1) return s;

  else return s[s.length()-1] + s.substr(0 , s.length()-1);

}

 

string func(string s , int idx , int len) {

  string ans = "";

  idx--;

  while(len >= 1) {

    ans += s[idx];

    idx--;

    len--;

  }

   string res = "";

  for(int i = ans.size()-1; i >= 0; i--) res += ans[i];

  return res;

}

 

signed main() {

  ios_base::sync_with_stdio(0);

  cin.tie(0);

 

  int t , n;

  cin >> t;

  while(t--) {

    string s;

    cin >> s >> n;

    vector<string> a(n);

    for(int i = 0; i < n; i++) cin >> a[i];

    map<string , int> map;

    for(int i = 0; i < n; i++) {

      int len = a[i].length();

      set<string> set;

      string left = a[i] , right = a[i];

      set.insert(a[i]);

      for(int j = 1; j <= 3; j++) {

        if(j <= len) {

         left = rotateleft(left);

          right = rotateright(right);

          set.insert(left) , set.insert(right);

        }

      }

      for(auto str : set) map[str]++;

    }

    vector<int> dp(s.length()+1 , 0);

    dp[0] = 1;

    for(int i = 1; i <= s.length(); i++) {

      for(int len = 1; len <= i; len++) {

        string str = func(s , i , len);

        dp[i] = dp[i] + map[str] * dp[i-len];

      }

    }

    cout << dp[s.length()] << "\n";

  }

  return 0;

}




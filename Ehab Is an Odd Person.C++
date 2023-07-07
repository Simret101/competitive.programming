#include <bits/stdc++.h>
using namespace std;
int main()
{
   int a;
   cin>>a;
   vector<int> ans(a);
   int b=0;
   int c=0;
  for(int i=0;i<a;i++){
    cin>> ans[i];
    if(ans[i]%2==0)
    {
        c++;
    }
    else{
        b++;
    }
  }
  if(c!=0 && b!=0)
  {
      sort(ans.begin(),ans.end());
      for(int i=0;i<a;i++){
        cout<<ans[i]<<" ";
      }
  }
  else{
    for(int i=0;i<a;i++){
    cout<<ans[i]<<" ";
  }}
  return 0;
}

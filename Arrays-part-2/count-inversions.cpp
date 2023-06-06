using ll = long long;
ll inv = 0;
void merge(ll low, ll mid, ll high, vector<ll> &arr){
    ll merged[high-low+1] = {0};
    ll i = low, j = mid+1, k = 0;

    while(i<=mid && j<=high){
        if(arr[i] <= arr[j]){
            merged[k] = arr[i];
            ++i;
        }
        else {
            inv += mid-i+1;
            merged[k] = arr[j];
            ++j;
        }
        ++k;
    }

    while(i<=mid){
        merged[k] = arr[i];
        ++i;
        ++k;
    }
    while(j<=high){
        merged[k] = arr[j];
        ++j;
        ++k;
    }

    for(i=0; i<high-low+1; ++i){
        arr[i+low] = merged[i];
    }


}



void mergeSort(ll low, ll high, vector<ll> &arr){
    if(low>=high)return;
    ll mid = low + (high-low)/2;
    mergeSort(low, mid, arr);
    mergeSort(mid+1, high, arr);

    merge(low,mid,high,arr);
}

ll getInversions(long long *arr, int n){
    vector<ll> nums;
    for(int i=0; i<n; ++i)nums.push_back(arr[i]);
    mergeSort(0,n-1,nums);
    return inv;
}

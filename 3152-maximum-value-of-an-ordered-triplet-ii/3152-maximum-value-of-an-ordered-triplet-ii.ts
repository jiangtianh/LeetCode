function maximumTripletValue(nums: number[]): number {
    const n = nums.length;
    const later = new Array(nums.length);
    
    let biggestLater = -1;
    for (let i = n-1; i >= 0; i--) {
        later[i] = biggestLater;
        biggestLater = Math.max(biggestLater, nums[i])
    };

    let res = 0;
    const stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && stack[stack.length-1] < nums[i]) {
            stack.pop();
        };
        stack.push(nums[i]);
        if (stack.length >= 2) {
            res = Math.max(res, (stack[0] - nums[i]) * later[i]);
        };
    };

    return res;
};
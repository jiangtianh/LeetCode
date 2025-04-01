function mostPoints(questions: number[][]): number {
    const d = {}
    const f = (i) => {
        if (i >= questions.length) {
            return 0
        } else if (i in d){
            return d[i]
        }
        const solve = questions[i][0] + f(i+questions[i][1]+1);
        const skip = f(i+1);
        const res = Math.max(solve, skip)
        d[i] = res
        return res
    }
    return f(0)
};
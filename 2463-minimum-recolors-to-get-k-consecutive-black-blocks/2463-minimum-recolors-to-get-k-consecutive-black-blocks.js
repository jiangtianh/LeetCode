/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function(blocks, k) {
    l = 0
    whiteCount = 0
    res = blocks.length + 1
    for (r = 0; r < blocks.length; r++) {
        if (blocks[r] == "W") {
            whiteCount += 1
        }
        if (r - l + 1 == k) {
            res = Math.min(res, whiteCount)
            if (blocks[l] == "W"){
                whiteCount -= 1
            }
            l += 1
        }


    }
    return res
};
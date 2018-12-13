# Measure of Sortedness - Spearman
# https://webuild.envato.com/blog/using-stats-to-not-break-search/

# xs & ys are arrays of results in order of rank
def spearman(xs, ys):
    # calculate the mean of each set of ranks (simple sum/length calculation)
    # as both are just the sum of ranks [1,2,3,4...] and have same length,
    # we can figure it out based on an arithmetic sum
    total = 0.5 * len(xs) * (len(xs)+ 1)
    x_mean = y_mean = total / len(xs)

    # initialize totals that we'll need
    sum_mean_diff = 0
    sum_x_mean_diff_sq = 0
    sum_y_mean_diff_sq = 0

    # sum the differences of the items
    xs.each_with_index do |x, x_rank|
        x_rank = x_rank + 1 # ranking is 1-based, not 0-based
        # grab the corresponding item from the other set of ranked items
        y_rank = ys.index(x) + 1

        # work out the error of each item from it's mean
        x_mean_diff = x_rank - x_mean
        y_mean_diff = y_rank - y_mean

        # aggregate totals for final calc
        sum_mean_diff += x_mean_diff * y_mean_diff
        sum_x_mean_diff_sq += x_mean_diff ** 2
        sum_y_mean_diff_sq += y_mean_diff ** 2
    end

    # final coefficient
    sum_mean_diff / Math.sqrt(sum_x_mean_diff_sq * sum_y_mean_diff_sq)
end
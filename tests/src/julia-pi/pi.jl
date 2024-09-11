# Estimate pi in parallel using multiple threads

using Base.Threads
using Random

# Calculate the number of points in the unit circle out of n points
function monte_carlo_pi_part(n)
    rng = Xoshiro()
    # If within the unit circle
    sum(rand(rng)^2 + rand(rng)^2 < 1 for i = 1:n)
end

# Estimate pi using n points
function est_pi(n)
    nt = nthreads()
    ps = zeros(nt)
    # Each thread gets (n / nt) number of points
    @threads for i in 1:nt
        ps[threadid()] += monte_carlo_pi_part(ceil(Int, n / nt))
    end
    est = 4 * (sum(ps) / n)
    println("Estimate of pi: ", est)
end

elapsed = @elapsed est_pi(5000000000)

println("Elapsed time: ", elapsed)

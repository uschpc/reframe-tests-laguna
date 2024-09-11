# Bootstrapping a GLM in parallel on multiple cores

library(parallel)

time <- system.time({
  trials <- 600000
  cores <- as.numeric(Sys.getenv("SLURM_CPUS_PER_TASK"))

  data <- iris[iris$Species != "setosa", c(1, 5)]
  data$Species <- factor(data$Species)
  
  model <- function(i, samp = data) {
    ind <- sample(nrow(samp), nrow(samp), replace = TRUE)
    results <- glm(samp[ind, 2] ~ samp[ind, 1], family = binomial(link = "logit"))
    coef(results)
  }

  coefs <- mclapply(1:trials, model, mc.cores = cores)
})

print(paste("Elapsed time:", time[["elapsed"]]))

library(latex2exp)

blocking <- c(4829.41,
              3294.8,
              2721.81,
              2424.59)

nonblocking <- c(9127.37,
                 4208.75,
                 6081.16,
                 3096.83,
                 3577.34)

boxplot(blocking, nonblocking, 
        main = TeX(r'($^{64}$Cu-PEG$_{4}$-RAP Blocking Study)'),
        at = c(1,2),
        las = 1,
        names = c("blocking", "nonblocking"),
        col = c("orange", "red"),
        border = "black",
        horizontal = TRUE,
        notch = FALSE,
        xlab = TeX(r'($^{64}$Cu-PEG$_{4}$-RAP Activity (counts))', bold = TRUE)
        )

x <- list(blocking, nonblocking)

stripchart(x,
           method = "overplot",
           add = TRUE, 
           col = c("black"),
           pch = 21,
           lwd = 1,
           bg = c("black")
          )

t.test(blocking, nonblocking, paired = FALSE)

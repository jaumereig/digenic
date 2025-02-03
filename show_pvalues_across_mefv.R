library("ggplot2")

mefv.247612295.nlrp3 <- read.csv("~/Escritorio/digenic/aux/nlrp3_247612295.mefv.pvalues.out", header = FALSE, sep = " ")
mefv.247612295.nlrp3 <- mefv.247612295.nlrp3[, -c(13, 14, 15)]
mefv.247612295.nlrp3[, 1:2] <- lapply(mefv.247612295.nlrp3[, 1:2], function(x) sub("-.*", "", x))
mefv.247612295.nlrp3 <- mefv.247612295.nlrp3[grepl("^(1:|16:)", mefv.247612295.nlrp3$V1) & grepl("^(1:|16:)", mefv.247612295.nlrp3$V2), ]
# Add the specified column names
colnames(mefv.247612295.nlrp3) <- c("NLRP3", "MEFV", "Obsmm", "ObsmM", "ObsMm", "ObsMM", "Expmm", "ExpmM", "ExpMm", "ExpMM", "chi2", "p-value")

mefv.247612295.nlrp3 <- mefv.247612295.nlrp3[order(mefv.247612295.nlrp3$MEFV), ]


mefv.247612295.nlrp3$log_pvalue <- log10(mefv.247612295.nlrp3$`p-value`)
mefv.247612295.nlrp3$log_pvalue[is.infinite(mefv.247612295.nlrp3$log_pvalue)] <- NA

ggplot(mefv.247612295.nlrp3, aes(x = MEFV, y = log_pvalue)) +
  geom_point() +
  labs(x = "Position in MEFV", y = "Log10(p-value)", title = "Log-transformed P-values across MEFV positions") +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 90, hjust = 0.5))


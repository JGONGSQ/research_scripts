fp_ind <- function(ind, nc) {
  
  tmp <- c(ind);
  i <- 1;
  while (i <= (nc-1)) {
    tmp <- c(tmp, ind);
    i <- i+1;
  }
  
  print(tmp);
  return (tmp);
  
}
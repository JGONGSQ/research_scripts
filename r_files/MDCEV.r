fp_ind <- function(index, nc) {
  # index: parameter, the index number
  # nc: parameter, the number of alternatives
  
  list <- c();
  i <- 1;
  
  while (i <= nc) {
    list <- c(list, index);
    i = i+1;
  }
  
  return (list);
}


parameter_ind <- function(ivgt, ind, nc, sero, ncoeffs) {
  
  i <- 1;
  while (i <= nc) {
    j <- 1;
    while (j <= ncoeffs[i]) {
      if (i > ind) {
        ivgt <- c(ivgt, sero);
      }
      if (i < ind) {
        ivgt <- c(sero, ivgt);
      }
      j <- j+1;
    }
    i <- i+1;
  }
  
  return (ivgt);
}



generate_ivdt_matrix <- function(list_index, nc, ivsero, ivuno){
  
  list <- c();
  i = 1;
  
  while (i <= nc) {
    if (i == (list_index -1)){
      list <- c(list, ivuno)
    }
    else {
      list <- c(list, ivsero)
    }
  }
  
  return (list)
}







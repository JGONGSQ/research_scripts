fp_index <- function(index, nc) {
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

f_index <- function(po, nc, index_of_outside_good){

    list <- c()
    i <- 1;

    while(i <= nc){

        if (i == 1){
            list <- c(list, index_of_outside_good)
        }
        else {
            list <- c(list, (po - 1 + i))
        }
        i = i + 1
    }

    return(list)
}

generate_ivdt_list <- function(index, nc, ivsero, ivuno){
  
  # initial the list
  list <- c();
  i = 1;
  
  while (i <= nc) {
    if (i == index){
      list <- c(list, ivuno)
    }
    else {
      list <- c(list, ivsero)
    }
    i = i + 1
  }
  
  return (list)
}

generate_ivd_matrix <- function(nc, ivsero, ivuno){

    # initial the list
    list <- c();
    i = 1;

    while(i <= nc) {
        temp = generate_ivdt_list(i, nc, ivsero, ivuno)
        list <- c(list, temp)
        i = i + 1
    }

    return (list)
}


generate_ivgt_list <- function(index, nc, ivsero, ivuno){

  # initial the list
  list <- c();
  i = 1;

  while (i <= nc) {
    if (i == index && i != 1){
      list <- c(list, ivuno)
    }
    else {
      list <- c(list, ivsero)
    }
    i = i + 1
  }
  return (list)
}

generate_ivg_matrix <- function(nc, ivsero, ivuno){

    # initial the list
    list <- c();
    i = 1;

    while(i <= nc) {
        temp = generate_ivgt_list(i, nc, ivsero, ivuno)
        list <- c(list, temp)
        i = i + 1
    }

    return (list)
}

generate_ivmt_list <- function(){

}


generate_ivm_matrix <- function(nc, ivsero){

    # initial the list
    list <- c();
    i = 1

    while(i <= nc){
        temp = generate_ivmt_list()
        list <- c(list, temp)
        i = i + 1
    }
    return(list)
}




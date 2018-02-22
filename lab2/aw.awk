BEGIN {q="["}

{q=q "[";
    for (i=2;i<NF;i++) q=q $i ", "; 
    q=q $NF; 
    q=q "], "}

END {print(substr(q,0,length(q) - 2) "]")}

program Solution;
var
    tActu, tFut, legume, price: Double;
begin
    read(tActu, tFut, legume);
    price := round((legume / (1 + tActu / 100) * (1 + tFut / 100)) * 100) / 100;
    writeln(price);
end.
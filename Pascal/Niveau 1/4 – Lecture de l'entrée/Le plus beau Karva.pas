program Solution;
var
   i, karvas, weight, age, longC, heiA: LongInt;
begin
   read(karvas);
   for i := 1 to karvas do
   begin
      read(weight, age, longC, heiA);
      writeln(longC * heiA + weight);
   end;
end.
program Solution;
var
   packages, weight: LongInt;
begin
   read(packages, weight);
   if packages * weight > 105 then
   begin
      writeln('Surcharge !');
   end
   else
   begin
      writeln;
   end;
end.
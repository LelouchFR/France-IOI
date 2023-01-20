program Solution;
var
   hour, price: integer;
begin
   read(hour);
   price := 10 + 5 * hour;
   if price > 53 then
   begin
      price := 53;
   end;
   writeln(price);
end.
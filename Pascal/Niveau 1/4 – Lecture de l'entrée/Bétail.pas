program Solution;
var
   nums, res, i: LongInt;
begin
   res := 0;
   for i := 1 to 20 do
   begin
      read(nums);
      res := res + nums;
   end;
   writeln(res);
end.
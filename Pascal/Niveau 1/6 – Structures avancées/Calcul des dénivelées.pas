program Solution;
var
    i, negSum, posSum, nums, num: LongInt;
begin
    negSum := 0;
    posSum := 0;
    read(nums);
    for i := 1 to nums do
    begin
        read(num);
        if num < 0 then
        begin
           negSum := negSum + num; 
        end
        else
        begin
            posSum := posSum + num;
        end;
    end;
    writeln(posSum);
    writeln(Abs(negSum));
end.
program Solution;
var
    Houses, absMin, absMax, ordMin, ordMax, abss, ords, i, larg, long: LongInt;
begin
    read(Houses);
    absMax := 1;
    ordMax := 1;
    absMin := 1000000;
    ordMin := 1000000;
    for i := 1 to Houses do
    begin
        read(abss, ords);
        if abss > absMax then
        begin
            absMax := abss;
        end
        else if abss < absMin then
        begin
            absMin := abss;
        end;
        if ords > ordMax then
        begin
           ordMax := ords; 
        end
        else if ords < ordMin then
        begin
            ordMin := ords;
        end;
    end;
    larg := absMax - absMin;
    long := ordMax - ordMin;
    if absMin > absMax then
    begin
        larg := absMin - absMax;
        writeln((2 * larg - 1) + (2 * long - 1));
    end
    else
    begin
        writeln((2 * larg) + (2 * long));
    end;
end.
program Solution;
var
    weights: array of Double;
    charretts, i: LongInt;
    totWeight, moyWeight: Double;
begin
    read(charretts);
    setLength(weights, charretts);
    totWeight := 0.0;
    for i := 0 to (charretts - 1) do
    begin
        read(weights[i]);
        totWeight := totWeight + weights[i];
    end;
    moyWeight := totWeight / charretts;
    for i := 0 to (charretts - 1) do
    begin
        writeln(moyWeight - weights[i] :0:10 );
    end;
end.
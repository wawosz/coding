function out = fitHill(conc, mu, st, fitN)

max0 = max(mu)*1.5;
kd0 = conc(1);
for i = 2:length(mu)
    if(mu(i) < (max0/2))
        kd0 = conc(i);
    end
end
n0 = 2;

if fitN == 0
    out = fminunc(@cost, [kd0 max0 n0]);
else
    out = fminunc(@cost2, [kd0 max0]);
    out = [out, fitN];
end

    function c = cost(kmn)
        
        thr = kmn(2) * 1./(1 + (kmn(1)./conc).^kmn(3));
        diff = thr - mu;
        normed = diff ./ st;
        c = 1e6*transpose(normed)*normed;
        
    end
    function c = cost2(km)
        
        thr = km(2) * 1./(1 + (km(1)./conc).^fitN);
        diff = thr - mu;
        normed = diff ./ st;
        c = 1e6*transpose(normed)*normed;
        
    end

SStot = sum((mu - mean(mu)).^2);

vals = out(2) * 1./(1 + (out(1)./conc).^out(3));
SSreg = sum((mu - vals).^2);

out = [out, (1 - SSreg/SStot)];
return;
end
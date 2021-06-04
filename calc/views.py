from django.shortcuts import render, redirect , HttpResponse
import math
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'calc/home.html')

#length contraction calculator
def lengthcontraction(request):
    try:
        Given = request.POST.get('Given','form1')
        l = request.POST.get('l')
        sr = request.POST.get('sr')
        v = request.POST.get('v')
        c=299792458
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        def meterconverter(lentype,lenn):
                if lentype == 'km':
                    m = lenn * 1000
                elif lentype == 'mm':
                    m = lenn / 1000
                elif lentype == 'cm':
                    m = lenn / 100.0
                elif lentype == 'in':
                    m = lenn / 39.37
                elif lentype == 'ft':
                    m = lenn / 3.28084
                elif lentype == 'yd':
                    m = lenn / 1.094
                elif lentype == 'mi':
                    m = lenn * 1609
                else:
                    m = lenn
                return m
        if request.method == "POST":
            if Given == 'form1' and l and v:
                lenn = float(request.POST['l'])
                velo = float(request.POST['v'])
                lentype = str(request.POST['l_op'])
                veltype = str(request.POST['v_op'])
                #convert length in meters
                lm = meterconverter(lentype,lenn)
                #convert velocity in meters
                if veltype == "km/s":
                    vm = velo *1000
                elif veltype == "mi/s":
                    vm = velo * 1609
                elif veltype == "c":
                    vm = velo * c
                else:
                    vm = velo 
                y = math.sqrt(1 - (vm**2/c**2))
                re = lm * y
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    startpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'m':re,'cm':re*100,'mm':re*1000,'km':re/1000,'in':re*39.37,'ft':re*3.28084,'yd':re*1.094,'mi':re/1609} 
                context = {
                'output': k1,
                'redict':redict,
                'y':y,
                'lm':lm,
                'vm':vm,
                'result':re,
                'l_op':lentype,
                'v_op':veltype,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'l':lenn,
                'v':velo,
                }
                return render(request,'calc/lengthcontraction.html',context)

            elif Given == 'form2' and sr and l:
                srlen = float(request.POST['sr'])
                lenn = float(request.POST['l'])
                srtype = str(request.POST['sr_op'])
                lentype = str(request.POST['l_op'])
                #convert relative length in meters
                srm = meterconverter(srtype,srlen)
                # convert length to meters
                lm = meterconverter(lentype,lenn)
                re = srm / lm
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    startpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'m/s':re,'km':re/1000,'mi/s':re*1609,'ligth speed':re/2.998e+8} 
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'redict':redict,
                'srm':srm,
                'lm':lm,
                'l_op':lentype,
                'sr_op':srtype,
                'result':re,
                'Given':Given,
                'l':lenn,
                'sr':srlen,
                }
                return render(request,'calc/lengthcontraction.html',context) 

            elif Given == 'form3' and sr and v:
                srlen = float(request.POST['sr'])
                velo = float(request.POST['v'])
                srtype = str(request.POST['sr_op'])
                veltype = str(request.POST['v_op'])
                #convert velocity in meters
                if veltype == "km/s":
                    vm = velo *1000
                elif veltype == "mi/s":
                    vm = velo * 1609
                elif veltype == "c":
                    vm = velo * c
                else:
                    vm = velo 
                #convert relative length in meters
                srm = meterconverter(srtype,srlen)
                y = math.sqrt(1-vm**2/c**2)
                re = srm / y
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    startpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'m':re,'cm':re*100,'mm':re*1000,'km':re/1000,'in':re*39.37,'ft':re*3.28084,'yd':re*1.094,'mi':re/1609} 
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'redict':redict,
                'srm':srm,
                'vm':vm,
                'v_op':veltype,
                'sr_op':srtype,
                'result':re,
                'Given':Given,
                'v':velo,
                'sr':srlen,
                }
                return render(request,'calc/lengthcontraction.html',context) 
        return render(request,'calc/lengthcontraction.html',{'Given':Given})
    except:
        messages.error(request, "Please enter valid data")
        return render(request,'calc/lengthcontraction.html',{'Given':Given})

#capacitance Calculator
def capacitance(request):
    try:
        Given = request.POST.get('Given','form1')
        a = request.POST.get('a')
        d = request.POST.get('d')
        c = request.POST.get('c')
        def zerocount(v):
            v = str(v)
            c=0
            for i in v:
                if i == '0':
                    c+=1
            return c
        def squareconverter(t,l):
            if t == 'mm':
                l = l / 0.000001
            elif t == 'cm':
                l = l / 10000
            elif t == 'in':
                  l = l/1550
            elif t == 'ft':
                l = l / 10.764
            elif t == 'yd':
                l = l / 1.196
            else:
                l = l
            return l
        def lengthconverter(t,l):
            if t == 'mm':
                l = l / 0.000001
            elif t == 'cm':
                l = l / 100.0
            elif t == 'um':
                l = l/1000000
            elif t == 'in':
                  l = l/39.37
            elif t == 'ft':
                l = l / 3.28084
            elif t == 'yd':
                l = l / 1.094
            elif t == 'mi':
                l = l * 1609
            else:
                l = l
            return l
        def faradconverter(t,l):
            if t == "nf":
                l = l / 1000000000
            elif t == "uf":
                l = l / 1000000
            elif t == "pf":
                l = l / 1000000000000
            elif t == "mf":
                l = l / 1000
            else:
                l = l
            return l 
        if request.method == "POST":
            if Given == "form1" and a and d:
                a = float(request.POST.get('a'))
                d = float(request.POST.get('d'))
                a_op = request.POST.get('a_op')
                d_op = request.POST.get('d_op')
                e = 8.854
                am = squareconverter(a_op,a)
                dm = lengthconverter(d_op,d)       
                c1 = (e*(am/dm))
                c = c1 * 0.000000000001
                print(c)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(c)
                if str(c) in 'e':
                    index_num = c.index('e')
                    startpoint = c[:index_num]
                    endpoint = c[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(c))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True

                redict = {'Farad (F)':c,'MilliFarad (mF)':c*1000,'MicroFarad (uF)':c*1000000,'NanoFarad (nF)':c*10000000000,'PicoFarad (pF)':c*1000000000000}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'a':a,
                'd':d,
                'e':e,
                'am':am,
                'dm':dm,
                'a_op':a_op,
                'd_op':d_op,
                'result':c,
                'Given':Given,
                'redict':redict
                }
                return render(request,'calc/capacitance.html',context)
            elif Given == "form2" and a and c:
                a = float(request.POST.get('a'))
                c = float(request.POST.get('c'))
                c_op = request.POST.get('c_op')
                a_op = request.POST.get('a_op')
                e = 8.854
                cm = faradconverter(c_op,c)
                am = squareconverter(a_op,a) 
                d = 8.854 * .000000000001 * am / cm
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(d)
                if str(d) in 'e':
                    index_num = d.index('e')
                    startpoint = d[:index_num]
                    endpoint = d[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(d))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                    
                redict = {'m':d,'mm':d*1000,'cm':d*100,'in':d*39.37,'ft':d*3.281,'yd':d*1.094
                ,'mi':d/1609}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'c':c,
                'a':a,
                'e':e,
                'cm':cm,
                'am':am,
                'c_op':c_op,
                'a_op':a_op,
                'result':d,
                'Given':Given,
                'redict':redict
                }
                return render(request,'calc/capacitance.html',context)
            elif Given == "form3" and c and d:
                c = float(request.POST.get('c'))
                d = float(request.POST.get('d'))
                c_op = request.POST.get('c_op')
                d_op = request.POST.get('d_op')
                e = 8.854
                cm = faradconverter(c_op,c)
                dm = lengthconverter(d_op,d)
                a = (dm*cm)/(8.854*0.000000000001)
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(a)
                if str(a) in 'e':
                    index_num = a.index('e')
                    startpoint = a[:index_num]
                    endpoint = a[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(a))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Sqaure Meters(m)':a,'Sqaure Millimeters(mm)':a*1000000,'Sqaure inches(in)':a*1550
            ,'Sqaure Yard(yd)':a*1.19599,'square feet(ft)':a*10.764}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'c':c,
                'd':d,
                'e':e,
                'cm':cm,
                'dm':dm,
                'c_op':c_op,
                'd_op':d_op,
                'result':a,
                'Given':Given,
                'redict':redict
                }
                return render(request,'calc/capacitance.html',context)

            return render(request,'calc/capacitance.html',{'Given':Given})
        else:
            return render(request,'calc/capacitance.html',{'Given':Given})
    except:
        messages.error(request,'Please enter valid data')
        return render(request,'calc/capacitance.html',{'Given':Given})

#Newton's Law of Cooling Calculator
def cooling(request):
    try:
        Given = request.POST.get('Given','form1')
        it = request.POST.get('it')
        at = request.POST.get('at')
        k = request.POST.get('k')
        tp = request.POST.get('tp')
        t = request.POST.get('t')

        if request.method == "POST":
            def zerocount(v):
                l = str(v).count('0')
                return int(l)
            def tempconverter(t,v):
                if t=='f':
                    c = (v-32) * 5/9
                elif t=='k':
                    c = v - 273.15
                else:
                    c = v
                return c
            def timeconverter(t,v):
                if t=='min':
                    c = v * 60
                elif t=='hrs':
                    c = v * 3600
                else:
                    c = v
                return c
            def powertimeconverter(t,v):
                if t=='min':
                    c = v * 0.016667
                elif t=='hrs':
                    c = v * 0.0002778
                else:
                    c = v
                return c
            if Given == "form1" and tp and k and at and it:
                it = float(request.POST.get('it'))
                at = float(request.POST.get('at'))
                k = float(request.POST.get('k'))
                tp = float(request.POST.get('tp'))
                it_op = request.POST.get('it_op')
                at_op = request.POST.get('at_op')
                k_op = request.POST.get('k_op')
                tp_op = request.POST.get('tp_op')
                #conver in celcius
                itc = tempconverter(it_op,it)
                atc = tempconverter(at_op,at)
                tps = timeconverter(tp_op,tp)
                ks = powertimeconverter(k_op,k)
                re = atc + (itc - atc) * math.exp(-ks*(tps))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    stratpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'°C':re,'°F':(re * 9/5) + 32 ,'K': re + 273.15}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'it':it,
                'at':at,
                'k':k,
                'ks':ks,
                'tp':tp,
                'it_op':it_op,
                'at_op':at_op,
                'k_op':k_op,
                'tp_op':tp_op,
                'result':re,
                'itc':itc,
                'atc':atc,
                'tps':tps,
                'redict':redict,
                }
                return render(request,'calc/cooling.html',context)
            elif Given == "form2" and tp and k and t and it:
                it = float(request.POST.get('it'))
                t = float(request.POST.get('t'))
                k = float(request.POST.get('k'))
                tp = float(request.POST.get('tp'))
                it_op = request.POST.get('it_op')
                t_op = request.POST.get('t_op')
                k_op = request.POST.get('k_op')
                tp_op = request.POST.get('tp_op')
                #conver in celcius
                itc = tempconverter(it_op,it)
                tc = tempconverter(t_op,t)
                #convert in sec
                tps = timeconverter(tp_op,tp)
                ks = powertimeconverter(k_op,k)
                
                re = tc - itc * math.exp(-ks*tps) 

                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    stratpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'°C':re,'°F':(re * 9/5) + 32 ,'K': re + 273.15}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'it':it,
                't':t,
                'k':k,
                'ks':ks,
                'tp':tp,
                'it_op':it_op,
                't_op':t_op,
                'k_op':k_op,
                'tp_op':tp_op,
                'result':re,
                'itc':itc,
                'tc':tc,
                'tps':tps,
                'redict':redict,
                }
                return render(request,'calc/cooling.html',context)
            elif Given == "form3" and tp and k and t and at:
                at = float(request.POST.get('at'))
                t = float(request.POST.get('t'))
                k = float(request.POST.get('k'))
                tp = float(request.POST.get('tp'))
                at_op = request.POST.get('at_op')
                t_op = request.POST.get('t_op')
                k_op = request.POST.get('k_op')
                tp_op = request.POST.get('tp_op')
                #conver in celcius
                atc = tempconverter(at_op,at)
                tc = tempconverter(t_op,t)
                #convert in sec
                tps = timeconverter(tp_op,tp)
                ks = powertimeconverter(k_op,k)
                re = atc + (tc-atc) * math.exp(-ks*(tps))
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    stratpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'°C':re,'°F':(re * 9/5) + 32 ,'K': re + 273.15}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'at':at,
                't':t,
                'k':k,
                'ks':ks,
                'tp':tp,
                'at_op':at_op,
                't_op':t_op,
                'k_op':k_op,
                'tp_op':tp_op,
                'result':re,
                'atc':atc,
                'tc':tc,
                'tps':tps,
                'redict':redict,
                }
                return render(request,'calc/cooling.html',context)
            elif Given == "form4" and tp and it and t and at:
                print("Form4")
                at = float(request.POST.get('at'))
                t = float(request.POST.get('t'))
                it = float(request.POST.get('it'))
                tp = float(request.POST.get('tp'))
                at_op = request.POST.get('at_op')
                t_op = request.POST.get('t_op')
                it_op = request.POST.get('it_op')
                tp_op = request.POST.get('tp_op')
                #conver in celcius
                atc = tempconverter(at_op,at)
                tc = tempconverter(t_op,t)
                itc = tempconverter(it_op,it)
                #convert in sec
                tps = timeconverter(tp_op,tp)
                re1 = (itc-atc)/(tc-atc)
                re = math.log(re1)/tps
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    stratpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Sec⁻¹':re,'Min⁻¹':re / 0.016667 ,'Hrs⁻¹': re / 0.0002778}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'at':at,
                't':t,
                'it':it,
                'itc':itc,
                'tp':tp,
                'at_op':at_op,
                't_op':t_op,
                'it_op':it_op,
                'tp_op':tp_op,
                'result':re,
                'ek':re1,
                'atc':atc,
                'tc':tc,
                'tps':tps,
                'redict':redict,
                }
                return render(request,'calc/cooling.html',context)
            elif Given == "form5" and k and it and t and at:
                
                at = float(request.POST.get('at'))
                t = float(request.POST.get('t'))
                it = float(request.POST.get('it'))
                k = float(request.POST.get('k'))
                at_op = request.POST.get('at_op')
                t_op = request.POST.get('t_op')
                it_op = request.POST.get('it_op')
                k_op = request.POST.get('k_op')
                #convert in celcius
                atc = tempconverter(at_op,at)
                tc = tempconverter(t_op,t)
                itc = tempconverter(it_op,it)
                #convert in sec
                ks = powertimeconverter(k_op,k)
                re1 = (itc-atc)/(tc-atc)
                re = math.log(re1)/ks
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(re)
                if str(re) in 'e':
                    index_num = re.index('e')
                    stratpoint = re[:index_num]
                    endpoint = re[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(re))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'Sec':re,'Min':re / 60 ,'Hrs': re / 3600}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                'Given':Given,
                'at':at,
                't':t,
                'it':it,
                'itc':itc,
                'k':k,
                'at_op':at_op,
                't_op':t_op,
                'it_op':it_op,
                'k_op':k_op,
                'result':re,
                'ek':re1,
                'atc':atc,
                'tc':tc,
                'ks':ks,
                'redict':redict,
                }
                return render(request,'calc/cooling.html',context)
            return render(request,'calc/cooling.html',{'Given':Given})
        else:
            return render(request,'calc/cooling.html',{'Given':Given})
    except:
        messages.error(request,'Please enter vaild data')
        return render(request,'calc/cooling.html',{'Given':'form1'})

#Thermal Conductivity Calculators
def thermalconduct(request):
    try:
        Given = request.POST.get('Given','form1')
        tc =request.POST.get('tc')
        t = request.POST.get('t')
        q = request.POST.get('q')
        d = request.POST.get('d')
        def zerocount(v):
            l = str(v).count('0')
            return int(l)
        def lengthconverter(t,l):
            if t == 'mm':
                l = l / 1000
            elif t=='km':
                l = l * 1000
            elif t == 'cm':
                l = l / 100.0
            elif t == 'in':
                l = l/39.37
            elif t == 'ft':
                l = l / 3.28084
            elif t == 'yd':
                l = l / 1.094
            elif t == 'mi':
                l = l * 1609
            else:
                l = l
            return l
        def tempconverter(t,v):
            l=0
            if t == 'f':
                l = (v - 32) * 5/9
            elif t == 'k':
                l = v - 273.15
            elif t == 'r':
                l = (v - 491.67) * 5/9
            elif t == 'de':
                l = 100 - v * 2 / 3
            elif t == 'n':
                l = v  / 0.33000
            elif t == 're':
                l = v *  5/4
            elif t == 'ro':
                l = v - 7.5 / 0.52500
            else:
                l = v
            return l


        if request.method == "POST":
            if Given == "form1" and tc and t and d :
                tc =float(request.POST.get('tc'))   
                t = float(request.POST.get('t'))
                d = float(request.POST.get('d'))
                t_op = request.POST['t_op']
                d_op = request.POST['d_op']
               
                #convert distance on meters
                dm = lengthconverter(d_op,d)
                tm = tempconverter(t_op,t)
        
                q = -(tc*tm)/dm
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(q)
                if str(q) in 'e':
                    index_num = q.index('e')
                    stratpoint = q[:index_num]
                    endpoint = q[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(q))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    't':t,
                    'd':d,
                    'tm':tm,
                    'tc':tc,
                    'dm':dm,
                    't_op':t_op,
                    'd_op':d_op,
                    'result':q,
                    'Given':Given
                    }
                return render(request,'calc/thermalconduct.html',context)
            elif Given == "form2" and q and t and tc :
                q =float(request.POST.get('q'))   
                t = float(request.POST.get('t'))
                tc = float(request.POST.get('tc'))
                t_op = request.POST['t_op']
                
                #convert distance on meters
                tm = tempconverter(t_op,t)
                d = -(tc*tm)/q
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(d)
                if str(d) in 'e':
                    index_num = d.index('e')
                    stratpoint = d[:index_num]
                    endpoint = d[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(d))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'m':d,'mm':d*1000,'cm':d*100,'km':d/1000,'mi':d/1609,'in':d*39.37,'ft':d*3.281
    ,'yd':d* 1.094}
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    't':t,
                    'tc':tc,
                    'q':q,
                    'tm':tm,
                    't_op':t_op,
                    'result':d,
                    'Given':Given,
                    'redict':redict
                    }
                return render(request,'calc/thermalconduct.html',context)
            elif Given == "form3" and q and t and d :
                q =float(request.POST.get('q'))   
                t = float(request.POST.get('t'))
                d = float(request.POST.get('d'))
                t_op = request.POST['t_op']
                d_op = request.POST['d_op']
                #convert distance on meters
                dm = lengthconverter(d_op,d)
                tm = tempconverter(t_op,t)
                tc = -(q*dm)/tm
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(tc)
                if str(tc) in 'e':
                    index_num = tc.index('e')
                    stratpoint = tc[:index_num]
                    endpoint = tc[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(tc))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                context = {
                    'output':k1,
                    'start':startpoint,
                    'end':endpoint,
                    't':t,
                    'd':d,
                    'q':q,
                    'tm':tm,
                    'dm':dm,
                    't_op':t_op,
                    'd_op':d_op,
                    'result':tc,
                    'Given':Given
                    }
                return render(request,'calc/thermalconduct.html',context)
            elif Given == "form4" and q and d and tc :
                q =float(request.POST.get('q'))   
                d = float(request.POST.get('d'))
                tc = float(request.POST.get('tc'))
                d_op = request.POST['d_op']
                
                #convert distance on meters
                dm = lengthconverter(d_op,d)
                t = (q*dm)/-tc
                k1 = False
                index_num = 0
                startpoint = 0
                endpoint = 0
                count = zerocount(t)
                if str(t) in 'e':
                    index_num = t.index('e')
                    stratpoint = t[:index_num]
                    endpoint = t[index_num+1:]
                    k1 = True
                elif count>5:
                    r11 = str("{:.2e}".format(t))
                    index_num = r11.index('e')
                    startpoint = r11[:index_num]
                    endpoint = r11[index_num+1:]
                    k1 = True
                redict = {'°C':t,'°F':(t * 9/5) + 32,'K':t+ 273.15,'°R':t*9/5 + 491.67,'°De':( 100 - t ) * 3 / 2,'°N':t* 0.33000,'°Re':t* 4/5
    ,'°Ro':t* 21/40 + 7.5}
                context = {
                'output':k1,
                'start':startpoint,
                'end':endpoint,
                    'dm':dm,
                    'd':d,
                    'tc':tc,
                    'q':q,
                    'd_op':d_op,
                    'result':t,
                    'Given':Given,
                    'redict':redict
                    }
                return render(request,'calc/thermalconduct.html',context)

        return render(request,'calc/thermalconduct.html',{'Given':Given})
    except:
        messages.error(request,'Please Enter Valid Data')
        return render(request,'calc/thermalconduct.html',{'Given':'form1'})
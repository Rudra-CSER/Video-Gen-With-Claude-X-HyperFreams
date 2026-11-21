scenes = [
 ("s01",0.0,6.0,[(0.3,3.8,"Your campus. Your food.\nA simpler way to order."),(3.9,5.9,"Meet Aarav, Nehru Hall.")]),
 ("s02",6.0,14.0,[(6.1,8.5,"SETU Food lists approved campus stalls."),(8.6,11.4,"They cook and deliver to your door."),(11.5,13.9,"You pay them directly. No commission.")]),
 ("s03",14.0,26.0,[(14.1,17.3,"For IIT Kharagpur campus accounts:\nstudents, faculty, staff."),(17.4,20.6,"Have an account? Sign in\nwith your password."),(20.7,23.5,"Or get a one-time code by email."),(23.95,25.95,"Six digits, and Aarav's in.")]),
 ("s04",26.0,33.0,[(26.1,28.9,"New here? Rewind to Aarav's day one."),(29.0,33.0,"An account takes a moment: name,\ninstitute email, phone, password.")]),
 ("s05",33.0,48.5,[(33.1,35.5,"Step two: where should orders arrive?"),(35.6,38.5,"Location access is optional.\nSearch works too."),(40.2,42.6,"Nehru Hall: inside the delivery area."),(42.7,46.3,"Check the pin, save it as Home,\nadd B-212.")]),
 ("s06",48.5,55.0,[(48.6,51.8,"Pick cuisines you like.\nThey show up first."),(51.9,54.7,"Then three things SETU does not do.")]),
 ("s07",55.0,67.5,[(55.1,57.5,"Good evening, Aarav. Tonight: dosa."),(61.4,63.4,"Southside Tiffins: approved by SETU."),(64.1,67.3,"Tap ADD: one Masala Dosa,\ntwo filter coffees.")]),
 ("s08",67.5,74.5,[(67.6,71.2,"Items ₹140, plus the stall's own\ndelivery charge: ₹10."),(71.3,74.45,"₹150, payable to the seller.\nNo platform fee.")]),
 ("s09",74.5,84.5,[(74.6,78.6,"Pay cash at your door,\nor scan the stall's QR."),(78.7,82.3,"With QR, the stall accepts first,\nthen you pay."),(82.85,84.45,"Aarav goes with cash.")]),
 ("s10",84.5,96.5,[(84.6,87.8,"Now follow along:\nconfirmed, cooking, on the way."),(89.2,92.4,"At the door, Aarav pays ₹150 in cash."),(92.5,96.5,"Then he tells them his code.\nThat completes the order.")]),
 ("s11",96.5,103.5,[(96.6,99.0,"Delivered. Five stars\nfor Southside Tiffins."),(99.1,101.9,"Something off? Report it\nfrom the order."),(102.0,103.4,"Dinner, sorted.")]),
 ("s12",103.5,112.0,[]),
]
prev_end=0.0; total=0; worst=0; prevcap=None; ok=True
for sid,a,b,caps in scenes:
    if abs(a-prev_end)>1e-9: print("GAP/OVERLAP before",sid,a,prev_end); ok=False
    prev_end=b; sw=0
    for (s,e,t) in caps:
        lines=t.split("\n"); w=len(t.split()); d=e-s; r=w/d
        sw+=w; worst=max(worst,r)
        flags=[]
        if s<a-1e-9 or e>b+1e-9: flags.append("OUTSIDE SCENE")
        if d<1.3: flags.append("SHORT")
        if r>2.6: flags.append("FAST")
        if len(lines)>2: flags.append("3 LINES")
        if max(len(l) for l in lines)>42: flags.append("LONG LINE")
        if prevcap and s<prevcap-1e-9: flags.append("OVERLAP")
        prevcap=e
        print(f"{sid} {s:6.2f}-{e:6.2f} {d:4.2f}s {w:2d}w {r:4.2f}w/s maxline {max(len(l) for l in lines):2d} {'!! '+','.join(flags) if flags else ''}")
        if flags: ok=False
    total+=sw
print("END",prev_end,"TOTAL WORDS",total,"worst w/s %.2f"%worst, "OK" if ok else "PROBLEMS")

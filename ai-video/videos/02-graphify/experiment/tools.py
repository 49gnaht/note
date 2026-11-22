import json, glob, os, sys, collections
D=os.path.dirname(os.path.abspath(__file__))
def proj(run):
    enc=os.path.join(D,'runs',run).replace('/','-').replace('.','-')
    c=glob.glob(os.path.expanduser('~/.claude/projects/')+enc)
    return c[0] if c else None
for j in sorted(glob.glob(os.path.join(D,'runs','*.json'))):
    run=os.path.basename(j)[:-5]; sid=json.load(open(j)).get('session_id')
    p=proj(run); f=os.path.join(p,sid+'.jsonl') if p else None
    if not f or not os.path.exists(f): print(run,'no transcript'); continue
    tools=collections.Counter(); gcmd=[]; hooks=0; inp=out=0
    for l in open(f):
        d=json.loads(l); m=d.get('message') or {}
        u=m.get('usage') or {}
        c=m.get('content')
        if isinstance(c,list):
            for b in c:
                if b.get('type')=='tool_use':
                    n=b['name']; cmd=(b.get('input') or {}).get('command','')
                    if n=='Bash' and cmd.strip().startswith('graphify'): n='graphify'; gcmd.append(cmd[:70])
                    elif n=='Bash': n='Bash:'+cmd.split()[0]
                    tools[n]+=1
        if 'hook additional context' in l or 'hook_additional_context' in l: hooks+=1
    print(f"{run:8} tools={dict(tools)} hooks={hooks}")
    for g in gcmd: print('     ',g)

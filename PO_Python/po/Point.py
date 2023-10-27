class Point: pass

def examine(un_point):
  return f"{un_point.nom} ({un_point.x},{un_point.y})"

def deplace(p, dx, dy):
    p.x += dx
    p.y += dy
    return f"{p.nom}({p.x},{p.y})"



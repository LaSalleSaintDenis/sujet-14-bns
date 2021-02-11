def recherche(elt, tab):
  ids = []
  for i in range(len(tab)):
    if elt == tab[i]:
      ids.append(i)
  return ids

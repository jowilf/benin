from time import sleep
import geonames.adapters.search
new_data = []
strip = lambda s: s.strip().split(":")
def read_data():
    with open('cotonou_q.data','r') as f:
        return list(map(strip,f.readlines()))
_USERNAME = 'kode'
final_result = []
for id,data in read_data():
    sa = geonames.adapters.search.Search(_USERNAME)
    result = sa.query(data).country('bj').execute()
    v = []
    for id_, name in result.get_flat_results():
        # make_unicode() is only used here for Python version-compatibility.
        #print(geonames.compat.make_unicode("[{0}]: [{1}]").format(id_, name))
        v.append("{0}#{1}".format(id_, name))
    if len(v)==0:
        final_result.append(f"{id},{data},mixed\n")
    else:
        final_result.append(f"{id},{data},{','.join(v)}\n")
    print(final_result[-1],end='')
    #sleep(0.)
with open('cotonou_q.result','w') as f:
    f.writelines(final_result)

def preorderTraverse(node):
    print(node['name'],node['data'], end=' ')  # Access this node's data.
    if len(node['children']) > 0:
        # RECURSIVE CASE
        for child in node['children']:
            preorderTraverse(child)  # Traverse child nodes.
    # BASE CASE
    return


if __name__ == "__main__":
    nodes = []
    nodes.append( {'name': '/', 'data' : [],'children': []} )
    nodes.append( {'name': 'a', 'data' : [],'children': []} )
    nodes.append( {'name': 'd', 'data' : [],'children': []} )
    nodes.append( {'name': 'e', 'data' : [],'children': []} )
    nodes[0]['children'] = [ nodes[1], nodes[2] ]
    nodes[1]['children'] = [ nodes[3]]
    nodes[0]['data'] = [ ['b.txt', 14848514], ['c.dat', 8504156] ]
    nodes[1]['data'] = [ ['f', 29116], ['g', 2557], ['h.lst', 62596] ]
    nodes[2]['data'] = [ ['j', 4060174], ['d.log', 8033020] ]
    nodes[3]['data'] = [ 'i', 584]

    for node in nodes:
        print('\n')
        preorderTraverse(node)
    print('\n')
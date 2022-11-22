# hubbard

This project computes the energy eigenvalue of the simple Hubbard Hamiltonian by using exact diagonalization.

## Table of contents.
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#how-to-use)
* [The group I want is not in groups.py ?](#the-group-i-want-is-not-in-groups.py-?)
* [Interraction matrix](#interraction-matrix)
* [Example of use](#example-of-use)
* [Inspiration](#inspiration)
* [Project status](#project-status)
## General info
This project was done during my 2022 summer intership.
	
## Technologies.
Project is created with:
* Python 3.10.4
* Numpy library
* sys library 
	
## How to use.
The program takes two entries as parameters. The number of electronics sites and the symmetry group under which you want to symmetrize the Hamiltonian. 

In the command line, it look like this:
python3 hubbard_diag_v5.py number of sites symmetry group

Example, if I want the eigenvalues for the two sites Hubbard Hamiltonian under the C2 symmetry group, it would look like this:
```
$ python3 hubbard_diag_v5.py 2 "c2"
```
The file groups.py contain some of the more common groups such that only typing the name as a string of the group under Schonflies convention is enough.
Current groups available are c2 (for 2,3,4 and 5 sites), c2v (4 sites), d3 (3 sites). It is quite easy to add new groups. 

## The group I want is not in groups.py ?
You need to add it. To add the group of your choice, go edit the function group_create in groups.py. You add an if statement to the function with the number of sites you want your group to act on and the name you want to give it when called in command line. 

You need to know how your group permute your sites. 

For example, the group c2 for 3 sites in a triangular configuration is symmetric under reflection of site 0 and site 1 along the axis of site 2.
You can imagine a triangle where sites number is assigned anti-clockwise. So, bottom left site is site 0, bottom right is site 1 and top site is site 2. 
Acting with c2 on this configuration would exchange site 0 with site 1 while letting site 2 at the top. 
Hence, the initial configuration [0,1,2] after c2 reflexion is now [1,0,2]. The latter list is the symmetry generator that you have to add to the function group_create in groups.py as sym_gen. 

Here, sym_gen is a list of lists because we can combine multiple symmetry generators to make more complicate groups. For example, we can create the non-abelian group d3 by combining the c2 symmetry generator [1,0,2] with c3 symmetry generator [2,0,1]:
```
def group_create(Nsites,group):
       if Nsites == 3 and group == "d3":        # add an if statement with the number of site and the name you want.
           sym_gen = [[1,0,2],[2,0,1]]          # add the symmetry generator that describe your group action.
           char_table = [[1,1,1,1,1,1],         # add the character table of the group.
                         [1,-1,1,-1,1,-1],
                         [2,0,-1,0,-1,0]]

```
As you see, you also need to give the character table of the group. Ultimately, it would be great if the program could generate the character table only from the symmetry generator, but for now we have to write it ourself. Also, it is important that the characters fit the group element order. 

## Example of use
So I want to know the eigenvalues of the 3 sites Hubbard Hamiltonian under symmetry group d3. Just type:
```
$ python3 hubbard_diag_v5.py 2 "c2"

```
and the program will return:

* The Hamiltonian matrix of the system. 
* All the sub-matrices in the symmetrized basis of the group.
* The total spin for each sub-matrices.
* The total number of electrons for each sub-matrices.
* The energy eigenvalues and eigenvectors of each sub-matrices


## Interaction matrix.
The program suppose that all the sites are interacting with each other. However, if this is not the case, you can write an interaction matrix.
For a 4 sites square system where there is no interaction between diagonals the interraction matrix would be as follow:
```
interaction_matrix = [[0,1,0,1],   (the zeroth sites does not interract with itself and with the second sites hence the 0 in the first row of matrix)
                      [1,0,1,0],   (Same pattern in other rows)
                      [0,1,0,1],
                      [1,0,1,0]]
```
## Inspiration.
This program has been inspired by annexe b of Dr Maxime Charlebois's PhD thesis: Théorie de champ moyen dynamique pour les systèmes inhomogènes.

## Project status.
Work in progress. Some changes has to be made to better suit non-abelian groups. 

## Acknowledgement.
Thanks to Dr Maxime Charlebois, my supervisor during this internship, for all his precious advices. 

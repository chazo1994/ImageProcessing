% Starter code prepared by James Hays for CS 143, Brown University

%This function will predict the category for every test image by finding
%the training image with most similar features. Instead of 1 nearest
%neighbor, you can vote based on k nearest neighbors which will increase
%performance (although you need to pick a reasonable value for k).

function predicted_categories = nearest_neighbor_classify(train_image_feats, train_labels, test_image_feats)
% image_feats is an N x d matrix, where d is the dimensionality of the
%  feature representation.
% train_labels is an N x 1 cell array, where each entry is a string
%  indicating the ground truth category for each training image.
% test_image_feats is an M x d matrix, where d is the dimensionality of the
%  feature representation. You can assume M = N unless you've modified the
%  starter code.
% predicted_categories is an M x 1 cell array, where each entry is a string
%  indicating the predicted category for each test image.

%{
Useful functions:
 matching_indices = strcmp(string, cell_array_of_strings)
   This can tell you which indices in train_labels match a particular
   category. Not necessary for simple one nearest neighbor classifier.

 D = vl_alldist2(X,Y) 
    http://www.vlfeat.org/matlab/vl_alldist2.html
    returns the pairwise distance matrix D of the columns of X and Y. 
    D(i,j) = sum (X(:,i) - Y(:,j)).^2
    Note that vl_feat represents points as columns vs this code (and Matlab
    in general) represents points as rows. So you probably want to use the
    transpose operator ' 
   vl_alldist2 supports different distance metrics which can influence
   performance significantly. The default distance, L2, is fine for images.
   CHI2 tends to work well for histograms.
 
  [Y,I] = MIN(X) if you're only doing 1 nearest neighbor, or
  [Y,I] = SORT(X) if you're going to be reasoning about many nearest
  neighbors 

%}
k = 5;
Msize = size(test_image_feats)
M = Msize(1)
d = Msize(2)
Nsize = size(train_image_feats)
N =Nsize(1)
X = train_image_feats';
Y = test_image_feats';
LB = train_labels;
D = vl_alldist2(Y,X);
predicted_categories = cell(M,1);
for i=1:M
  [TMP,I] = sort(D(i,:));
  labs = cell(k,1);
  for j=1:k
    pos = I(j);
    labs{j} = train_labels{pos};
  end
  labs
  frequent = cell(k,1);
  pos = 1
  for j=1:k
      numfre = 0;
      for l=1:k
       if strcmp(labs{j},labs{l})
           numfre = numfre + 1;
       end
      end
    frequent{j} = numfre;
  end
  
  [TEMP,ITER] = sort([frequent{:}]) ;
  predicted_categories{i} = labs{ITER(k)};
end
predicted_categories;



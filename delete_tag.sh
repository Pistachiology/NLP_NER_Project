for entry in `ls tag_per_v2_u8`
do
    cat ./tag_per_v2_u8/$entry | sed 's/(per)//g' | sed 's/(per_start)//g' | sed 's/(per_cont)//g' | sed 's/(per_end)//g' | sed 's/(loc)//g' \
        | sed 's/(loc_start)//g'| sed 's/(loc_cont)//g' | sed 's/(loc_end)//g' | sed 's/(org)//g' | sed 's/(org_start)//g' | sed 's/(org_cont)//g' \
        | sed 's/(org_end)//g' > ./untag_per_v2_u8/$entry
done
